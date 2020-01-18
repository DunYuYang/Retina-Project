#! R8
# -*- coding: utf-8 -*-
# R8 - AI Server - Version 19.18 - © 2004-2019 LEADERG INC. All Rights Reserved
# Please use OpenR8 to edit this file.


import R8_lib


if __name__ == '__main__':

	res = 0
	r8h = 0

	res = R8_lib.InitLib()
	if res <= 0 :
		exit

	r8h = R8_lib.New()


	# Variables

	R8_lib.AddVariable(r8h, "arg", "String", "")

	R8_lib.AddVariable(r8h, "image", "String", "--image=")

	R8_lib.AddVariable(r8h, "path", "String", "src/surgery.py")

	R8_lib.AddVariable(r8h, "result", "String", "")

	R8_lib.AddVariable(r8h, "space", "String", " ")

	R8_lib.AddVariable(r8h, "train", "String", "splash")

	R8_lib.AddVariable(r8h, "weights", "String", "--weights=")

	R8_lib.AddVariable(r8h, "weights_name", "String", "data/mask20181217T0933/mask_rcnn_mask_0020.h5")

	R8_lib.AddVariable(r8h, "image_path", "String", "data/pill/train/pill1.JPG")

	R8_lib.AddVariable(r8h, "result1", "Int", "0")

	R8_lib.AddVariable(r8h, "flowFilePath", "String", "../Python/checkIsPythonInstalled.flow")

	R8_lib.AddVariable(r8h, "flowFilePath1", "String", "../Python/checkIsTensorflowInstalled.flow")


	# Functions

	R8_lib.AddFunction2(r8h, "String_Add", "inference", "arg", "arg", "train")

	R8_lib.AddFunction2(r8h, "String_Add", "space", "arg", "arg", "space")

	R8_lib.AddFunction2(r8h, "String_Add", "--weights=", "arg", "arg", "weights")

	R8_lib.AddFunction2(r8h, "String_Add", "weights_name", "arg", "arg", "weights_name")

	R8_lib.AddFunction2(r8h, "String_Add", "space", "arg", "arg", "space")

	R8_lib.AddFunction2(r8h, "String_Add", "--image=", "arg", "arg", "image")

	R8_lib.AddFunction2(r8h, "String_Add", "image_path", "arg", "arg", "image_path")

	R8_lib.AddFunction(r8h, "python", "result", "path", "arg", None)


	# Run

	R8_lib.Run(r8h, 0)

	R8_lib.Release(r8h)

