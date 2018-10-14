import os



def sudo_cmd(cmd):
    sudoPassword = 'hello'
    os.system('echo %s|sudo -S %s' % (sudoPassword, cmd))

def read_bound_randomSeed(exname,filename,k):
    print exname
    cwd = os.getcwd()
    os.chdir(filename+"patch")
    sudo_cmd("./patch_cmd.sh > tmp_log")
    os.chdir(filename)
    os.system("cp *.c ../../benchmarks/gsl_src/gsl-2.1-repair/specfunc")
    os.chdir(cwd)
    sudo_cmd("./make_install.sh > tmp_log")
    sudo_cmd("rm tmp_log")


def generate_fpcore(a):
    cwd = os.getcwd()
    print cwd
    path = cwd+"/driver_functions/exe"
    os.chdir(path)
    file_list = []
    level_name = ["Low_level","Middle_level","High_level"]
    name = level_name[a-1]
    for file in os.listdir(path):
        if file.endswith(".out"):
            file_list.append(file)
    os.system("cp ../input/"+str(a)+"/*.txt ./")
    for i in file_list:
        cmd = cwd + "/herbgrind/herbgrind.sh ./"+i
        os.system(cmd)
    os.system("rm *.txt")
    os.system("rm -rf "+name)
    os.system("mkdir " + name)
    os.system("cp *.gh " + name + "/")
    return 0
os.chdir("driver_functions")
os.system("make")
os.system("cp *.out exe/")
os.system("rm *.out")
os.chdir("..")
# generate_fpcore(1)
# generate_fpcore(2)
# generate_fpcore(3)
