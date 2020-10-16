class Leads(object):
    def __init__(self, client):
        self._client = client

    def get_lead(self, lead_id, **kwargs):
        url = 'leads/{}'.format(lead_id)
        return self._client._get(self._client.BASE_URL + url, **kwargs)

    def get_all_leads(self, **kwargs):
        url = 'leads'
        return self._client._get(self._client.BASE_URL + url, **kwargs)

    def get_leadLabels(self, **kwargs):
        url = 'leadLabels'
        return self._client._get(self._client.BASE_URL + url, **kwargs)

    def get_one_leadLabel(self, lead_id, **kwargs):
        url = 'leads/{}'.format(lead_id)
        return self._client._get(self._client.BASE_URL + url, **kwargs)

    def get_leadSources(self, **kwargs):
        url = 'leadSources'
        return self._client._get(self._client.BASE_URL + url, **kwargs)

    def create_lead(self, data, **kwargs):
        url = 'leads'
        return self._client._post(self._client.BASE_URL + url, json=data, **kwargs)

    def create_leadLabel(self, data, **kwargs):
        url = 'leadLabels'
        return self._client._post(self._client.BASE_URL + url, json=data, **kwargs)

    def delete_lead(self, lead_id, **kwargs):
        url = 'leads/{}'.format(lead_id)
        return self._client._delete(self._client.BASE_URL + url, **kwargs)

    def delete_leadLabel(self, lead_id, **kwargs):
        url = 'leadLabels/{}'.format(lead_id)
        return self._client._delete(self._client.BASE_URL + url, **kwargs)

    def update_lead(self, lead_id, data, **kwargs):
        url = 'leads/{}'.format(lead_id)
        return self._client._put(self._client.BASE_URL + url, json=data, **kwargs)

    def update_leadLabel(self, lead_id, data, **kwargs):
        url = 'leadLabels/{}'.format(lead_id)
        return self._client._put(self._client.BASE_URL + url, json=data, **kwargs)