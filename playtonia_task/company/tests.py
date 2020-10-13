from django.test import TestCase
from rest_framework.test import APIClient
import json
from rest_framework import status
# Create your tests here.


class TestEmployees(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.companyPayload={
            "id":1,
            "name": "test_Playtonia01",
            "contact_no": "9999999999",
            "address": "sdfdsfsa"
        }
        request = self.client.post('/api/company/', json.dumps(self.companyPayload), content_type='application/json')
        self.assertEqual(request.status_code, status.HTTP_201_CREATED)
        self.Epmloyeepayload = {
            "id": 1,
            "Fname": "smuthu",
            "Lname": "V S",
            "salary": 30000,
            "contact_no": "9999999999",
            "address": "chennai-102",
            "companyName": self.companyPayload.get('id')
        }
        request = self.client.post(path='/api/emplyees/',
                                   data=json.dumps(self.Epmloyeepayload), content_type='application/json')
        self.assertEqual(request.status_code, status.HTTP_201_CREATED)

    def test_create_company_positive(self):
        payload={
            "name": "test_Playtonia01",
            "contact_no": "9999999999",
            "address": "sdfdsfsa"
        }
        request = self.client.post('/api/company/', json.dumps(payload),content_type='application/json')
        self.assertEqual(request.status_code, status.HTTP_201_CREATED)

    def test_create_company_failure(self):
        #contact number
        negative_payload={
            "name": "test_Playtonia01",
            "contact_no": "s9999999999",
            "address": "sdfdsfsa"
        }
        request = self.client.post('/api/company/', json.dumps(negative_payload),content_type='application/json')
        self.assertEqual(request.status_code, status.HTTP_400_BAD_REQUEST)

        # empty field
        negative_payload = {
            "name": "",
            "contact_no": "9999999999",
            "address": "sdfdsfsa"
        }
        request = self.client.post('/api/company/', json.dumps(negative_payload), content_type='application/json')
        self.assertEqual(request.status_code, status.HTTP_400_BAD_REQUEST)

        # all field required
        negative_payload = {
            "contact_no": "9999999999",
            "address": "sdfdsfsa"
        }
        request = self.client.post('/api/company/', json.dumps(negative_payload), content_type='application/json')
        self.assertEqual(request.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_company_positives(self):
        request = self.client.get('/api/company/'+str(self.companyPayload.get('id'))+'/')
        self.assertEqual(request.status_code, status.HTTP_200_OK)

    def test_get_company_failure(self):
        request = self.client.get('/api/company/5/')
        self.assertEqual(request.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_company_positives(self):
        request = self.client.delete('/api/company/'+str(self.companyPayload.get('id'))+'/')
        self.assertEqual(request.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_company_failure(self):
        request = self.client.delete('/api/company/5/')
        self.assertEqual(request.status_code, status.HTTP_404_NOT_FOUND)

    def test_patch_company_positives(self):
        payload={
            "address": "chennai-12"
        }
        request = self.client.patch('/api/company/1/',json.dumps(payload),content_type='application/json')
        self.assertEqual(request.status_code, status.HTTP_200_OK)

    def test_put_company_failure(self):
        payload={
            "address": "chennai-12"
        }
        request = self.client.put('/api/company/'+str(self.Epmloyeepayload.get('id'))+'/',json.dumps(payload),content_type='application/json')
        self.assertEqual(request.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_emplyees(self):

        payload={
            "id":2,
    "Fname": "smuthu",
    "Lname": "V S",
    "salary": 30000,
    "contact_no": "9999999999",
    "address": "chennai-102",
    "companyName": self.companyPayload.get('id')
}
        request = self.client.post(path='/api/emplyees/',
                              data=json.dumps(payload),content_type='application/json')
        self.assertEqual(request.status_code, status.HTTP_201_CREATED)

    def test_create_emplyees_failure(self):
        payload = {
        "id": 2,
        "Fname": "smuthu",
        "Lname": "V S",
        "salary": 30000,
        "contact_no": "9999999999",
        "address": "",
        "companyName": self.companyPayload.get('id')
            }
        request = self.client.post(path='/api/emplyees/',
                                   data=json.dumps(payload), content_type='application/json')
        self.assertEqual(request.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_emplyees(self):
        request = self.client.get('/api/emplyees/2/')
        print(request)
        self.assertEqual(request.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_emplyees(self):
        request = self.client.delete('/api/emplyees/'+str(self.Epmloyeepayload.get('id'))+'/')
        print(request)
        self.assertEqual(request.status_code, status.HTTP_204_NO_CONTENT)

    def test_patch_emplyees(self):
        payload={
            "address": "chennai-12"
        }
        request = self.client.patch('/api/emplyees/'+str(self.Epmloyeepayload.get('id'))+'/',json.dumps(payload),content_type='application/json')
        print(request)
        self.assertEqual(request.status_code, status.HTTP_200_OK)
