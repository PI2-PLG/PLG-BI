from modules.models import Module, ModuleData
import string

names = ['Modulo-FGA-A','Modulo-FGA-B','Modulo-FGA-C','Modulo-FGA-D']

print("Creating Modules...",end="")
modules = []
for index in range(4):
    mod = Module(name=names[index])
    mod.save()
    modules.append(mod)
print(" OK")



module_A_datas = [
                  ['2019-10-28 12:30:00-0300',-15.990043,-48.046277,32.1,25.5,890.0,50],
                  ['2019-10-28 13:00:00-0300',-15.990043,-48.046277,32.1,25.5,890.0,60],
                  ['2019-10-28 13:30:00-0300',-15.990043,-48.046277,33.0,25.5,890.0,50],
                  ['2019-10-28 14:00:00-0300',-15.990043,-48.046277,33.0,25.5,890.0,60],
                  ['2019-10-28 14:30:00-0300',-15.990043,-48.046277,33.0,25.5,890.0,50]
                 ]

module_B_datas = [
                  ['2019-10-28 12:30:00-0300',-15.990846,-48.045164,32.5,24.5,890.0,50],
                  ['2019-10-28 13:00:00-0300',-15.990846,-48.045164,32.5,24.5,890.0,60],
                  ['2019-10-28 13:30:00-0300',-15.990846,-48.045164,32.5,24.5,890.0,50],
                  ['2019-10-28 14:00:00-0300',-15.990846,-48.045164,32.5,24.5,890.0,60],
                  ['2019-10-28 14:30:00-0300',-15.990846,-48.045164,33.0,24.5,890.0,50],
                 ]

module_C_datas = [
                  ['2019-10-28 12:30:00-0300',-15.989804,-48.043127,32.1,24.5,890.0,50],
                  ['2019-10-28 13:00:00-0300',-15.989804,-48.043127,32.1,24.5,890.0,60],
                  ['2019-10-28 13:30:00-0300',-15.989804,-48.043127,33.1,24.5,890.0,50],
                  ['2019-10-28 14:00:00-0300',-15.989804,-48.043127,33.1,24.5,890.0,60],
                  ['2019-10-28 14:30:00-0300',-15.989804,-48.043127,33.3,24.5,890.0,50],
                 ]

module_D_datas = [
                  ['2019-10-28 12:30:00-0300',-15.988280,-48.044277,33.0,25.0,890.0,50],
                  ['2019-10-28 13:00:00-0300',-15.988280,-48.044277,33.0,25.0,890.0,60],
                  ['2019-10-28 13:30:00-0300',-15.988280,-48.044277,33.0,25.0,890.0,50],
                  ['2019-10-28 14:00:00-0300',-15.988280,-48.044277,33.0,25.0,890.0,60],
                  ['2019-10-28 14:30:00-0300',-15.988280,-48.044277,33.0,25.0,890.0,50],
                 ]

print("Creating ModuleDatas...",end="")
for index in range(5):
    dataA = ModuleData.objects.create(
                      date=module_A_datas[index][0],
                      latitude=module_A_datas[index][1],
                      longitude=module_A_datas[index][2],
                      temperature=module_A_datas[index][3],
                      humidity=module_A_datas[index][4],
                      velocity=module_A_datas[index][5],
                      ppm=module_A_datas[index][6],
                      module=modules[0]
                     )
    #dataA.save()
    modules[0].module_data.add(dataA)

    dataB = ModuleData.objects.create(
                      date=module_B_datas[index][0],
                      latitude=module_B_datas[index][1],
                      longitude=module_B_datas[index][2],
                      temperature=module_B_datas[index][3],
                      humidity=module_B_datas[index][4],
                      velocity=module_B_datas[index][5],
                      ppm=module_B_datas[index][6],
                      module=modules[1]
                     )
    #dataB.save()
    modules[1].module_data.add(dataB)

    dataC = ModuleData.objects.create(
                      date=module_C_datas[index][0],
                      latitude=module_C_datas[index][1],
                      longitude=module_C_datas[index][2],
                      temperature=module_C_datas[index][3],
                      humidity=module_C_datas[index][4],
                      velocity=module_C_datas[index][5],
                      ppm=module_C_datas[index][6],
                      module=modules[2]
                     )
    #dataC.save()
    modules[2].module_data.add(dataC)

    dataD = ModuleData.objects.create(
                      date=module_D_datas[index][0],
                      latitude=module_D_datas[index][1],
                      longitude=module_D_datas[index][2],
                      temperature=module_D_datas[index][3],
                      humidity=module_D_datas[index][4],
                      velocity=module_D_datas[index][5],
                      ppm=module_D_datas[index][6],
                      module=modules[3]
                     )
    #dataD.save()
    modules[3].module_data.add(dataD)
print(" OK")
