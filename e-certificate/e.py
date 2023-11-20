import cv2

list_of_names = []

def cleanup_data():
    with open("name-data.txt") as f:
        for line in f:
            list_of_names.append(line.strip())
           
            
def generate_certificates():
  
  for name in list_of_names:
      template = cv2.imread("certificate-template.jpg")
      cv2.putText(template,name , (413,673), cv2.FONT_HERSHEY_SIMPLEX, 5, (0, 0, 250), 5, cv2.LINE_AA)
      cv2.imwrite(f'generated-certificate-data/{name}.jpg',template)
cleanup_data()
generate_certificates()

print("Progesseing Complete")