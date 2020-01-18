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

	R8_lib.AddVariable(r8h, "dataset", "String", "--dataset=")

	R8_lib.AddVariable(r8h, "result", "String", "")

	R8_lib.AddVariable(r8h, "space", "String", " ")

	R8_lib.AddVariable(r8h, "train", "String", "train")

	R8_lib.AddVariable(r8h, "weights", "String", "--weights=")

	R8_lib.AddVariable(r8h, "weights_name", "String", "coco")

	R8_lib.AddVariable(r8h, "path", "String", "src/surgery.py")

	R8_lib.AddVariable(r8h, "dataset_path", "String", "data/pill/")

	R8_lib.AddVariable(r8h, "result1", "Int", "0")

	R8_lib.AddVariable(r8h, "flowFilePath", "String", "../Python/checkIsPythonInstalled.flow")

	R8_lib.AddVariable(r8h, "flowFilePath1", "String", "../Python/checkIsTensorflowInstalled.flow")


	# Functions

	R8_lib.AddFunction2(r8h, "String_Add", "train", "arg", "arg", "train")

	R8_lib.AddFunction2(r8h, "String_Add", "space", "arg", "arg", "space")

	R8_lib.AddFunction2(r8h, "String_Add", "--dataset=", "arg", "arg", "dataset")

	R8_lib.AddFunction2(r8h, "String_Add", "dataset_path", "arg", "arg", "dataset_path")

	R8_lib.AddFunction2(r8h, "String_Add", "space", "arg", "arg", "space")

	R8_lib.AddFunction2(r8h, "String_Add", "--weights=", "arg", "arg", "weights")

	R8_lib.AddFunction2(r8h, "String_Add", "weights_name", "arg", "arg", "weights_name")

	R8_lib.AddFunction(r8h, "python", "result", "path", "arg", None)


	# Run

	R8_lib.Run(r8h, 0)

	R8_lib.Release(r8h)

