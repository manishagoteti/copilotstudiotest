from azure.storage.blob import BlobServiceClient
import os
import Constants

# Create a BlobServiceClient
blob_service_client = BlobServiceClient.from_connection_string(Constants.connection_string)

# Get container clients for both containers
container1_client = blob_service_client.get_container_client(Constants.container1_name)
container2_client = blob_service_client.get_container_client(Constants.container2_name)

# Initialize dictionaries to store blob URLs and titles for both containers
container1_info = {'url': [], 'title1': []}
container2_info = {'title2': []}

# List all blobs in container1 and store their URLs and titles without extensions
blobs_list1 = container1_client.list_blobs()
for blob1 in blobs_list1:
    blob_client1 = container1_client.get_blob_client(blob1)
    title_1= os.path.splitext(blob1.name)[0] # Remove the extension
    container1_info['url'].append(blob_client1.url)
    container1_info['title1'].append(title_1)

# List all blobs in container2 and store their titles without extensions
blobs_list2 = container2_client.list_blobs()


# Map titles of container1 with container2 and create metadata for matching blobs

def addmedatatoblob():
    for blob2 in blobs_list2:
        print("-----blob2", blob2)
        title_2 = os.path.splitext(blob2.name.split('/')[-1])[0]
        if title_2 in container1_info['title1']:
            index = container1_info['title1'].index(title_2)
            url = container1_info['url'][index]
            blob_client2 = container2_client.get_blob_client(blob2.name)
            metadata = {'url': url, 'title':title_2}
            blob_client2.set_blob_metadata(metadata)
    status = "Ok"
    print("completed")
    return status

x = addmedatatoblob()

