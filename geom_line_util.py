#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import rpy2.robjects as robj
import rpy2.robjects.pandas2ri
from rpy2.robjects.packages import importr


def header_csv_plot(InputFilePath, PlotFilePath, x_axis, y_axis, fill):
    Data = pd.read_csv(InputFilePath)
    print(Data)

    r_script = """
  library(ggplot2)

  function(df){
    cCyan <- "#00a0e9"
    cMagenta <- "#e4007f"
    cGreen <- "#009944"
    cOrange <- "#f39800"
    cLightBlue <- "#0068b7"

    cols <- c("Cautious-Point"=cCyan, "Cautious-Distance"=cOrange, "Bold-Point"=cGreen, "Bold-Distance"=cMagenta)

    g <- ggplot(df,
    aes(
      x = WorldType,
      y = val,
      group = factor(Agent_type),
      colour = factor(Agent_type)
    )
  )
  g <- g +
  geom_line()+
  scale_fill_manual(values = cols)+
  labs(colour = 'Agent Type')+
  theme(legend.position = "top")+
  xlim("Prolific World", "Static World", "Dynamic World")+
  #軸ラベルのフォントサイズ調節
  theme(axis.title.x = element_text(size=18),axis.title.y = element_text(size=18))+
  #軸目盛りのフォントサイズ調節
  theme(axis.text.x = element_text(size=18),axis.text.y = element_text(size=18))+
  #凡例タイトルとラベルのフォントサイズ調節
  theme(legend.title = element_text(size=18),legend.text = element_text(size=18))

  ggsave(file='%s', plot=g, width=16, height=9)
  }
  """ % PlotFilePath

    plotFunc = robj.r(r_script)

    robj.pandas2ri.activate()
    testData_R = robj.conversion.py2ri(Data)

    plotFunc(testData_R)


def xy_list_categorise_length_plot(XList, YList, CategoriseList, WorkNameList, PlotFilePath, x_axis_name, y_axis_name):

    extention_split = PlotFilePath.split(".")
    data_export_path = ".".join(extention_split[:-1]) + ".csv"
    print(data_export_path)
    Data = pd.DataFrame({'plots': XList, 'characters': YList, 'length_of_plot': CategoriseList, 'work_name': WorkNameList})
    print(Data)
    Data.to_csv(data_export_path, index=False)

    r_script = """
        library(ggplot2)

        function(df){{
            cCyan <- "#00a0e9"
            cMagenta <- "#e4007f"
            cGreen <- "#009944"
            cOrange <- "#f39800"
            cLightBlue <- "#0068b7"

            #cols <- c("Cautious-Point"=cCyan, "Cautious-Distance"=cOrange, "Bold-Point"=cGreen, "Bold-Distance"=cMagenta)

            g <- ggplot(df,
                aes(
                    x = plots,
                    y = characters,
                    group = factor(length_of_plot),
                    colour = factor(length_of_plot)
                )
            )
            #quartzFonts(HiraMaru=quartzFont(rep("HiraMaruProN-W4", 4)))
            g <- g +
            geom_line()+
            #theme_gray(base_family = "Japan1GothicBBB")+
            theme_gray(base_family = "HiraKakuProN-W3")+
            xlab('{x_axis_name}')+
            ylab('{y_axis_name}')



            ggsave(file='{FilePath}', plot=g, width=16, height=9)
        }}
        """.format(
            FilePath=PlotFilePath,
            x_axis_name=x_axis_name,
            y_axis_name=y_axis_name)

    plotFunc = robj.r(r_script)

    robj.pandas2ri.activate()
    testData_R = robj.conversion.py2ri(Data)

    plotFunc(testData_R)


def xy_list_categorise_works_plot(XList, YList, CategoriseList, WorkNameList, PlotFilePath, x_axis_name, y_axis_name):

    extention_split = PlotFilePath.split(".")
    data_export_path = ".".join(extention_split[:-1]) + ".csv"
    print(data_export_path)
    Data = pd.DataFrame({'plots': XList, 'characters': YList, 'length_of_plot': CategoriseList, 'work_name': WorkNameList})
    print(Data)
    Data.to_csv(data_export_path, index=False)

    r_script = """
        library(ggplot2)
        library(grid)

        function(df){{
            cCyan <- "#00a0e9"
            cMagenta <- "#e4007f"
            cGreen <- "#009944"
            cOrange <- "#f39800"
            cLightBlue <- "#0068b7"

            g <- ggplot(df,
                aes(
                    x = plots,
                    y = characters,
                    group = work_name,
                    #colour = work_name
                )
            )
            g <- g +
            geom_line(colour = cOrange, alpha = 0.2, size = 1.5,
                arrow = arrow(angle = 15, type = "closed"))+
            theme_gray(base_family = "HiraKakuProN-W3")+
            xlab('{x_axis_name}')+
            ylab('{y_axis_name}')



            ggsave(file='{FilePath}', plot=g, units = "cm", width=32, height=18, device=cairo_ps)
        }}
        """.format(
            FilePath=PlotFilePath,
            x_axis_name=x_axis_name,
            y_axis_name=y_axis_name)

    plotFunc = robj.r(r_script)

    robj.pandas2ri.activate()
    testData_R = robj.conversion.py2ri(Data)

    plotFunc(testData_R)


#if __name__ == '__main__':
#    InputFilePath = ""
#    PlotFilePath = ""

#    x_axis = ""
#    y_axis = ""
#    fill = ""

#    header_csv_plot(InputFilePath, PlotFilePath, x_axis, y_axis, fill)
