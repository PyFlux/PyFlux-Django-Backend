from django.db.models import Q

class DatatableMixin(object):
    """ JSON data for datatables
    """
    model = None
    columns = []
    order_columns = []
    max_display_length = 100  # max limit of records returned, do not allow to kill our server by huge sets of data
    pre_camel_case_notation = False  # datatables 1.10 changed query string parameter names
    none_string = ''
    escape_values = True  # if set to true then values returned by render_column will be escaped
    
    @property
    def _querydict(self):
        return self.request.data

    def get_columns(self):
        """ Returns the list of columns that are returned in the result set
        """
        return self.columns

    def render_column(self, row, column):
        """ Renders a column on a row. column can be given in a module notation eg. document.invoice.type
        """
        # try to find rightmost object
        obj = row
        parts = column.split('.')
        for part in parts[:-1]:
            if obj is None:
                break
            obj = getattr(obj, part)

        # try using get_OBJECT_display for choice fields
        if hasattr(obj, 'get_%s_display' % parts[-1]):
            value = getattr(obj, 'get_%s_display' % parts[-1])()
        else:
            value = getattr(obj, parts[-1], None)

        if value is None:
            value = self.none_string

        #if self.escape_values:
        #    value = escape(value)
            
        if value and hasattr(obj, 'get_absolute_url'):
            return '<a href="%s">%s</a>' % (obj.get_absolute_url(), value)
        return value

    def ordering(self, qs):
        sorting_cols = len(self._querydict['order'])
        order = []
        order_columns = self.order_columns
        for i in range(sorting_cols):
            sort_col = self._querydict['order'][i]['column']
            sort_dir = self._querydict['order'][i]['dir'] # sorting order, eg: asc
            sdir = '-' if sort_dir == 'desc' else ''
            sortcol = order_columns[sort_col]
            if not sortcol: continue
            if isinstance(sortcol, list):
                for sc in sortcol:
                    order.append('{0}{1}'.format(sdir, sc.replace('.', '__')))
            else:
                order.append('{0}{1}'.format(sdir, sortcol.replace('.', '__')))

        if order:
            return qs.order_by(*order)
        return qs

    def paging(self, qs):
        limit = min(int(self._querydict.get('length', 10)), self.max_display_length)
        start = int(self._querydict.get('start', 0))

        # if pagination is disabled ("paging": false)
        if limit == -1:
            return qs
        return qs[start:start + limit]

    def get_initial_queryset(self):
        if not self.model:
            raise NotImplementedError("Need to provide a model or implement get_initial_queryset!")
        return self.model.objects.all()
        
    def extract_datatables_column_data(self):
        """ Helper method to extract columns data from request as passed by Datatables 1.10+
        """
        columns = self._querydict['columns']
        col_data = []
        for i in range(len(columns)):
            col_data.append({'name':columns[i]['name'],
                             'data': columns[i]['data'],
                             'searchable': columns[i]['searchable'],
                             'orderable': columns[i]['orderable'],
                             'search.value': columns[i]['search']['value'],
                             'search.regex': columns[i]['search']['regex'],
                             })
            
        return col_data

    def filter_queryset(self, qs):
        # print(self._querydict)
        """ If search['value'] is provided then filter all searchable columns using istartswith
        """
        columns = self.get_columns()
        
        # get global search value
        search = self._querydict['search']['value'] #self._querydict.get('search[value]', None)
        col_data = self.extract_datatables_column_data()
        q = Q()
        for col_no, col in enumerate(col_data):
            # apply global search to all searchable columns
            if search and col['searchable']:
                q |= Q(**{'{0}__istartswith'.format(columns[col_no].replace('.', '__')): search})

            # column specific filter
            if col['search.value']:
                qs = qs.filter(**{
                    '{0}__istartswith'.format(columns[col_no].replace('.', '__')): col['search.value']})
        return qs.filter(q)

    def prepare_results(self, qs):
        data = []
        for item in qs:
            data.append([self.render_column(item, column) for column in self.get_columns()])
        return data

    def handle_exception(self, e):
        # logger.exception(str(e))
        raise e

    def get_context_data(self, *args, **kwargs):
        try:     
            qs = self.get_initial_queryset()

            # number of records before filtering
            total_records = qs.count()

            qs = self.filter_queryset(qs)

            # number of records after filtering
            total_display_records = qs.count()

            qs = self.ordering(qs)
            qs = self.paging(qs)

            # prepare output data
            
            data = self.prepare_results(qs)

            return {'draw': int(self._querydict.get('draw', 0)),
                   'recordsTotal': total_records,
                   'recordsFiltered': total_display_records,
                   'data': data                   
                   }
        except Exception as e:
            return self.handle_exception(e)