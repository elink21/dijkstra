import cx_Freeze
executables = [cx_Freeze.Executable("grafos.py", base = None, icon = None)]
build_exe_options = {"packages": ["cv2","numpy"],"include_files":[]}
cx_Freeze.setup(name = "Caminos mas cortos",version = "1.0",description = "Algoritmo de dijkstra",options={"build_exe": build_exe_options},executables = executables)