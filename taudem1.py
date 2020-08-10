import os
import subprocess


def taudem_execute(taudem_cmd):
    p = subprocess.Popen(
        taudem_cmd,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)
    output = p.communicate()[0].decode('utf-8')
    print(output)


def pitremove(np, input, output):
    """ command: pitremove -z dem.tif -fel demfel.tif, demfile: input elevation grid, felfile: output elevations with pits filled """
    pitremove = "mpirun -np {} pitremove -z {} -fel {}".format(
        np, input, output)
    return pitremove


def d8flowdir(np, input, output1, output2):
    """ command: d8flowdir -fel demfel.tif -p demp.tif -sd8 demsd8.tif, demfile: Pit filled elevation input data, pointfile: D8 flow directions output, slopefile: D8 slopes output """
    d8flowdir = "mpirun -np {} d8flowdir -fel {} -p {} -sd8 {}".format(
        np, input, output1, output2)
    return d8flowdir


def dinfflowdir(np, input, output1, output2):
    """ command: dinfflowdir -fel demfel.tif -ang demang.tif -slp demslp.tif, demfile: Pit filled elevation input data, angfile: Dinf flow directions output, slopefile: Dinf slopes output """
    dinfflowdir = "mpirun -np {} dinfflowdir -fel {} -ang {} -slp {}".format(
        np, input, output1, output2)
    return dinfflowdir


def aread8(np, input, output):
    """ command: aread8 -p demp.tif -ad8 demad8.tif [-o outletfile.shp] [-wg demwg.tif] [-nc], pfile: input flow directions grid, ad8file: output contributing area grid, Outletfile: input outlets shapefile, wgfile: input weight grid file  """
    aread8 = "mpirun -np {} aread8 -p {} -ad8 {}".format(
        np, input, output)
    return aread8


def areadinf(np, input, output):
    """ command: areadinf -ang demang.tif -sca demsca.tif [-o outletfile.shp] [-wg demwg.tif] [-nc], angfile: Dinf angles input file, scafile: Dinf contributing areas output file, outletfile: Shapefile with outlet coordinates, wgfile: an optional weight file for area computations """
    areadinf = "mpirun -np {} areadinf -ang {} -sca {}".format(
        np, input, output)
    return areadinf
