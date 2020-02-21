import unittest
import statusdb.db.utils as utils
import os
import mock
import couchdb

class TestUtils(unittest.TestCase):
    def test_load_couch_server_valid(self):
        path = os.path.dirname(os.path.abspath(__file__))
        valid_config_file = os.path.join(path, '../test_data/test_statusdb.yaml')
        couch = utils.load_couch_server(valid_config_file)
        assert couch is not None

    def test_load_couch_server_invalid(self):
        path = os.path.dirname(os.path.abspath(__file__))
        invalid_config_file = os.path.join(path, '../test_data/test_statusdb_invalid.yaml')
        with self.assertRaises(RuntimeError):
            couch = utils.load_couch_server(invalid_config_file)

    def test_find_or_make_key_without_key(self):
        made_key = utils.find_or_make_key(None)
        assert len(made_key) == 32

    def test_find_or_make_key_with_key(self):
        found_key = utils.find_or_make_key('3c46730b395e4a728e1993c069a7eb70')
        assert found_key == '3c46730b395e4a728e1993c069a7eb70'

    def test_comp_obj(self):
        dict1 = {"a": 1, "b": 2}
        dict2 = {"a": 1, "b": 2}
        dict3 = {"a": 1, "b": 3}
        dict4 = {"a": 1}
        dict5 = {'entity_type': 'project_summary'}
        self.assertTrue(utils.comp_obj(dict1, dict2))
        self.assertFalse(utils.comp_obj(dict1, dict3))
        self.assertFalse(utils.comp_obj(dict1, dict4))

    def test_dont_load_status_if_20158_not_found(self):
        obj = {'samples': {'x': {'status': 'doc_not_found', 'm_reads_sequenced': 'doc_not_found'},
                           'y': {'status': 'some_status', 'm_reads_sequenced': 10},
                           'z': {'some_other_key': 'blah'},
                           'missing_sample': {'status': 'doc_not_found', 'm_reads_sequenced': 'doc_not_found', 'other_key': 'ok'}}}

        dbobj = {'samples': {'x': {'status': 'ok', 'm_reads_sequenced': 5},
                           'y': {'status': 'some_other_status', 'm_reads_sequenced': 15},
                           'z': {'some_other_key': 'blah'}}}
        updated_obj = utils.dont_load_status_if_20158_not_found(obj, dbobj)
        print(updated_obj)
        expected_obj = {'samples': {'x': {'status': 'ok', 'm_reads_sequenced': 5},
                                    'y': {'status': 'some_status', 'm_reads_sequenced': 10},
                                    'z': {'some_other_key': 'blah'},
                                    'missing_sample': {'other_key': 'ok'}}}
        self.assertEqual(updated_obj, expected_obj)

    def test_find_proj_from_view(self):
        #FIXME
        db = mock.Mock()
        db.view = lambda db_name: {db_name: 'x'}
        result = utils.find_proj_from_view(db, 'p1')
        print(result)
        pass

    def test_find_proj_from_samp(self):
        #FIXME
        pass

    def test_find_samp_from_view(self):
        #FIXME
        pass

    def test_find_flowcell_from_view(self):
        #FIXME
        pass

    def test_find_sample_run_id_from_view(self):
        #FIXME
        pass

    def test_calc_avg_qv(self):
        #FIXME
        pass

    def test_get_qc_data(self):
        #FIXME
        pass

    def test_get_scilife_to_customer_name(self):
        #FIXME
        pass

#    @mock.patch('statusdb.db.couchdb.Server')
#    def test_save_couchdb_obj(self, mock_couch):
#        mock_couch.return_value = {'some_database': {'object': {'_id': 'some_id'}}}
#        mock_couch.return_value.save = True
#        test_url = 'http://some.test.url'
#        connection = couchdb.Server(url=test_url)
#        db = connection['some_database']
#        db = {'some_database': {'object': {'_id': 'some_id'}}}
#        obj = {'storage_status': 'status', '_id': 'some_id'}
#        result = utils.save_couchdb_obj(db, obj)
#        print(result)
#        pass

