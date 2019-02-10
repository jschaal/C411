# 02/10/19 09:20 AM

import copy
import csv

from BaseDataTable import BaseDataTable
from DerivedDataTable import DerivedDataTable


class CSVDataTable(BaseDataTable):
    """
    The implementation classes (XXXDataTable) for CSV database, relational, etc. will extend the
    base class and implement the abstract methods.
    """

    def __init__(self, table_name, connect_info, key_columns=None, debug=True):
        """

        :param table_name: Name of the table. This is the table name for an RDB table or the file name for
            a CSV file holding data.
        :param connect_info: Dictionary of parameters necessary to connect to the data. See examples in subclasses.
        :param key_columns: List, in order, of the columns (fields) that comprise the primary key.
            A primary key is a set of columns whose values are unique and uniquely identify a row. For Appearances,
            the columns are ['playerID', 'teamID', 'yearID']
        :param debug: If true, print debug messages.
        """

        super().__init__(table_name, connect_info, key_columns, debug)

        fn = self._connect_info['directory'] + "/" + self._connect_info["file_name"]

        # opening up your csv files as a csv file
        # in that location, open up this file as a scv file

        with open(fn, 'r') as csv_file:

            # reading csv file
            # DictReader is a method of csv
            reader = csv.DictReader(csv_file, delimiter=',', quotechar='"')

            # use a for loop and get them into our lists

            # something that characterizes a player is the player ID
            # in a dictionary we have {UNI:'mg3740'}
            # dictionaries have a key:value pair

            self._rows = None
            self._header = None

            for row in reader:

                if self._header is None:
                    self._header = row.keys()

                # check the column names
                # if there's no column names, set the columns
                # as the keys of the row
                if self._key_columns is None:
                    self._key_columns = list(row.keys())

                if self._rows is None:
                    # fill up an empty array
                    self._rows = []
                self._rows.append(row)

    def __str__(self):
        result = "CSVDataTable: name = " + self._table_name
        result += "\nconnect_info = " + str(self._connect_info)
        result += "\nkey_columns = " + str(self._key_columns)
        result += "\nHeader = " + str(self._header)

        if self._rows is not None:
            result += "\nNo of rows = " + str(len(self._rows))
            to_print = min(len(self._rows), 5)
            for i in range(0, to_print):
                result += "\n" + str(self._rows[i])
        else:
            result += "NO ROWS FOOL!"

        return result

    def matches_template(self, row, template):

        keys = list(template.keys())

        for k in keys:

            # doesn't match the template
            v = row.get(k, None)
            if template[k] != v:
                return False

        return True

    #  Helper function to make a template from key fields
    def makeTemplateFromKeys(self, key_fields):
        """
        :param key_fields: The values for the key_columns, in order, to use to find a record. For example,
            for Appearances this could be ['willite01', 'BOS', '1960']
        """

        template = {}
        for keyNum in range(0, len(self._key_columns)):
            template[self._key_columns[keyNum]] = key_fields[keyNum]

        return template

    # Helper function to return a list of rows satisfying a template
    def getRows_by_template(self, template, field_list=None, limit=None, offset=None, order_by=None):
        """
        :param template: A dictionary of the form { "field1" : value1, "field2": value2, ...}. The function will return
            a derived table containing the rows that match the template.
        :param field_list: A list of requested fields of the form, ['fielda', 'fieldb', ...]
        :param limit: Do not worry about this for now.
        :param offset: Do not worry about this for now.
        :param order_by: Do not worry about this for now.
        :return: A list of rows matching the template
        """

        result = None

        if self._rows is not None and template is not None:
            # select statement in SQL

            result = []

            # go from 0 to the length of the rows
            for i in range(0, len(self._rows)):

                # check if a row matches a template using a new method
                if self.matches_template(self._rows[i], template):
                    if field_list == None:
                        result.append(self._rows[i])
                    else:
                        outRow = {}
                        for field in field_list:
                            if field in field_list:
                                outRow[field] = self._rows[i][field]
                        result.append(outRow)
        return result

    def find_by_primary_key(self, key_fields, field_list=None):
        """

        :param key_fields: The values for the key_columns, in order, to use to find a record. For example,
            for Appearances this could be ['willite01', 'BOS', '1960']
        :param field_list: A subset of the fields of the record to return. The CSV file or RDB table may have many
            additional columns, but the caller only requests this subset.
        :return: None, or a dictionary containing the columns/values for the row.
        """

        template = self.makeTemplateFromKeys(key_fields)

        return self.find_by_template(template, field_list)

    def find_by_template(self, template, field_list=None, limit=None, offset=None, order_by=None):
        """

        :param template: A dictionary of the form { "field1" : value1, "field2": value2, ...}. The function will return
            a derived table containing the rows that match the template.
        :param field_list: A list of requested fields of the form, ['fielda', 'fieldb', ...]
        :param limit: Do not worry about this for now.
        :param offset: Do not worry about this for now.
        :param order_by: Do not worry about this for now.
        :return: A derived table containing the computed rows.
        """

        result = self.getRows_by_template(template, field_list, limit, offset, order_by)

        final_result = DerivedDataTable("FBT:" + self._table_name, result, self._connect_info, self._key_columns,
                                        self._debug)
        self._lastQuery = result

        return final_result

    def insert(self, new_record):
        """

        :param new_record: A dictionary representing a row to add to the set of records. Raises an exception if this
            creates a duplicate primary key.
        :return: None
        """

        # check to see if the primmary key already exists
        tmp = {}
        for keyNum in range(len(self._key_columns)):
            tmp[self._key_columns[keyNum]] = new_record[self._key_columns[keyNum]]

        r = self.getRows_by_template(tmp, self._key_columns)

        if len(r) > 0:
            raise ValueError('primary key already exists.  Record not inserted. Keys = {}'.format(tmp))

        self._rows.append(new_record)

    def delete_by_template(self, template):
        """

        Deletes all records that match the template.

        :param template: A template.
        :return: A count of the rows deleted.
        """

        deleteCount = 0
        deleteList = []
        if self._rows is not None and template is not None:

            i = 0

            while i < len(self._rows):
                # check if a row matches a template using a new method
                if self.matches_template(self._rows[i], template):
                    self._rows.pop(i)
                    deleteCount += 1
                else:
                    i += 1

        return deleteCount

    def delete_by_key(self, key_fields):
        """

        Deletes all records that match the template.

        :param key_fields: List containing the values for the key columns
        :return: A count of the rows deleted.
        """

        template = self.makeTemplateFromKeys(key_fields)

        deleteCount = 0
        if self._rows is not None and template is not None:

            # go from 0 to the length of the rows
            for i in range(0, len(self._rows)):

                # check if a row matches a template using a new method
                if self.matches_template(self._rows[i], template):
                    self._rows.pop(i)
                    deleteCount += 1
                    break

        return deleteCount

    def update_by_template(self, template, new_values):
        """

        :param template: A template that defines which matching rows to update.
        :param new_values: A dictionary containing fields and the values to set for the corresponding fields
            in the records. This returns an error if the update would create a duplicate primary key. NO ROWS are
            update on this error.
        :return: The number of rows updates.
        """

        # create a list of new primary keys after proposed update and see if any are already present
        # first find primary keys for records in template
        rows = self.getRows_by_template(template)
        valueColumns = list(new_values.keys())

        for row in copy.copy(rows):
            keyChanged = False
            for key in self._key_columns:
                if key in valueColumns:
                    keyChanged = True
                    row[key] = new_values[key]
                if keyChanged:
                    k = self.find_by_primary_key(list(row.values()))
                    if len(k) > 0:
                        raise ValueError('primary key already exists.  Record not inserted. Keys = {}', row)

        updateCount = 0
        for row in rows:
            for key in list(new_values.keys()):
                row[key] = new_values[key]
            updateCount += 1

        return updateCount

    def update_by_key(self, key_fields, new_values):
        """

        :param key_fields: List of values for primary key fields
        :param new_values: A dictionary containing fields and the values to set for the corresponding fields
            in the records. This returns an error if the update would create a duplicate primary key. NO ROWS are
            update on this error.
        :return: The number of rows updates.
        """
        template = self.makeTemplateFromKeys(key_fields)
        return self.update_by_template(template, new_values)
