from dipy.io.image import load_nifti, save_nifti


def intensify_image(in_file, out_file, scalar):
    # load image from nifti
    data, affine, img = load_nifti(in_file, return_img=True)
    # scale image
    scaled_data = data * scalar
    # save image back to file
    save_nifti(out_file, scaled_data, affine)
