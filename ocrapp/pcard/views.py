from .ocr import ocr


def ocr_core(img, info):
    extracted_data = ocr('media/' + img.instance.image.name)
    info.image_id = img.instance.id
    info.name = extracted_data['Name']
    info.fname = extracted_data['Father Name']
    info.dob = extracted_data['Date of Birth']
    info.pan = extracted_data['PAN']
    info.save()
