from selenium import webdriver
from PIL import Image
import os
import time
import math


def fullpage_screenshot(driver, file):
	js = "window.document.styleSheets[0].insertRule(" +
			"'::-webkit-scrollbar {display: none;}', " + \
			"window.document.styleSheets[0].cssRules.length);"
	driver.execute_script(js)

	vp_total_height = driver.execute_script("return document.body.parentNode.scrollHeight")
	vp_height = driver.execute_script("return window.innerHeight")
	vp_width = driver.execute_script("return window.innerWidth")
	scale = driver.execute_script("return window.devicePixelRatio")

	rectangles_vp = []

	vp = 0
	while vp < vp_total_height:
		vp_top_height = vp + vp_height

		if vp_top_height > vp_total_height:
			vp = vp_total_height - vp_height
			vp_top_height = vp_total_height

		rectangles_vp.append((0, vp, 0, vp_top_height))
		vp = vp + vp_height

	stitched_image = Image.new(
								'RGB',
								(int(vp_width * scale), int(vp_total_height * scale))
							)

	for i, rect_vp in enumerate(rectangles_vp):
		driver.execute_script("window.scrollTo({0}, {1})".format(0, rect_vp[1]))
		time.sleep(0.2)

		tmpfile = "part_{0}.png".format(i)
		driver.get_screenshot_as_file(tmpfile)
		screenshot = Image.open(tmpfile)

		if (i + 1) * vp_height > vp_total_height:
			offset = (0, int((vp_total_height - vp_height) * scale))
		else:
			offset = (0, int(i * vp_height * scale - math.floor(i / 2.0)))

		stitched_image.paste(screenshot, offset)

		del screenshot
		os.remove(tmpfile)

	stitched_image.save(file)
	del stitched_image
	return True
