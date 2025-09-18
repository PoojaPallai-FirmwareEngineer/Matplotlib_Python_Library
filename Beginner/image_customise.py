# Program: Image Life Cycle Demonstration using Matplotlib

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Load the image from file (stored as a NumPy array)
img = mpimg.imread("/home/ppallai/Programs/Libraries/Matplotlib/Beginner/ada.jpg")
# print(img) Instead of writing print we can plt.imshow()

# Display the original image
imgplt = plt.imshow(img)
plt.title("Original Image")
plt.show()

# Extract one channel (Red) to create a pseudo grayscale image
lum_img = img[:,:,0]
plt.imshow(lum_img)
plt.title("Pseudo Grayscale (Red Channel)")
plt.show()

# Color change for the image. Apply a colormap ("hot") to the grayscale image
plt.imshow(lum_img, cmap='hot')
plt.title("Grayscale with 'Hot' Colormap")
plt.show()

# NOTE: We can change the color maps on the existing plot objects using set underscore cmap method
# Change colormap dynamically using set_cmap()
imgplt = plt.imshow(lum_img)
imgplt.set_cmap("nipy_spectral")
plt.title("Colormap Changed Dynamically → 'nipy_spectral'")
plt.show()

# Add a colorbar to show intensity-color mapping
imgplt = plt.imshow(lum_img)
plt.title("Image with Colorbar")
plt.colorbar()
plt.show()

# To enhance the contrast in your image or expand the contrast in a particular region while
# scarifing the detail in colors that don't match that don't very match or don't matter.
# Tool to find interesting regions in the histogram use his function
# Plot histogram of pixel intensities to analyze contrast
plt.hist(lum_img.ravel(), bins=256, range=(0.0,1.0), fc='k', ec='k')
plt.title("Histogram of Pixel Intensities")
plt.show()

# Adjust contrast by setting color limits (clim)
imgplt = plt.imshow(lum_img, clim = (0.0, 0.7))
plt.title("Contrast Adjustment (clim = 0.0 → 0.7)")
plt.show()

# Compare "Before" and "After" contrast adjustment
fig = plt.figure()

# Left subplot (Before adjustment)
a = fig.add_subplot(1, 2, 1)
imgplt = plt.imshow(lum_img)
a.set_title("Before Contrast Adjustment")
plt.colorbar(ticks = [0.1, 0.3, 0.5, 0.7], orientation='horizontal')

# Right subplot (After adjustment with clim)
a = fig.add_subplot(1,2,2)
imgplt = plt.imshow(lum_img)
imgplt = plt.clim(0.0, 0.7)
a.set_title("After Contrast Adjustment")
plt.colorbar(ticks = [0.1, 0.3, 0.5, 0.7], orientation='horizontal')

plt.suptitle("Before vs After Contrast Stretching", fontsize=14)  # overall title
plt.show()

