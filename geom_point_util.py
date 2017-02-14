import numpy as np
import pandas as pd
import rpy2.robjects as robj
import rpy2.robjects.pandas2ri
from rpy2.robjects.packages import importr


def xy_list_plot(XList, YList, PlotFilePath, x_axis_name, y_axis_name):

    extention_split = PlotFilePath.split(".")
    data_export_path = ".".join(extention_split[:-1]) + ".csv"
    print(data_export_path)
    Data = pd.DataFrame({'characters': XList, 'works': YList})
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

            g <- ggplot(df, aes(x=characters, y=works))

            g <- g +
            geom_point(colour = cLightBlue, size = 0.5)+
            xlab('{x_axis_name}')+
            ylab('{y_axis_name}')

            ggsave(file='{FilePath}', plot=g, width=16, height=5)
        }}
    """.format(
            FilePath=PlotFilePath,
            x_axis_name=x_axis_name,
            y_axis_name=y_axis_name
        )

    #print(r_script)

    plotFunc = robj.r(r_script)

    robj.pandas2ri.activate()
    testData_R = robj.conversion.py2ri(Data)

    plotFunc(testData_R)


def pos_deg_distribution_plot(Data, PlotFilePath, x_axis_name, y_axis_name):
    extention_split = PlotFilePath.split(".")
    data_export_path = ".".join(extention_split[:-1]) + ".csv"
    print(data_export_path)
    # print(Data)
    Data.to_csv(data_export_path, index=False)

    r_script = """
        library(ggplot2)

        function(df){{
            cCyan <- "#00a0e9"
            cMagenta <- "#e4007f"
            cGreen <- "#009944"
            cOrange <- "#f39800"
            cLightBlue <- "#0068b7"

            g <- ggplot(df, aes(x=position, y=average_degree))

            g <- g +
            geom_point(colour = cLightBlue, size = 2)+
            xlab('{x_axis_name}')+
            ylab('{y_axis_name}')

            ggsave(file='{FilePath}', plot=g, width=10, height=5)
        }}
    """.format(
            FilePath=PlotFilePath,
            x_axis_name=x_axis_name,
            y_axis_name=y_axis_name
        )

    #print(r_script)

    plotFunc = robj.r(r_script)

    robj.pandas2ri.activate()
    testData_R = robj.conversion.py2ri(Data)

    plotFunc(testData_R)


def read_csv_xy_universal_plot(DataPath, x_data_name, y_data_name, x_axis_name, y_axis_name):
    # print(Data)
    Data = pd.read_csv(DataPath)
    extention_split = DataPath.split(".")
    PlotFilePath = ".".join(extention_split[:-1]) + ".eps"

    r_script = """
        library(ggplot2)

        function(df){{
            cCyan <- "#00a0e9"
            cMagenta <- "#e4007f"
            cGreen <- "#009944"
            cOrange <- "#f39800"
            cLightBlue <- "#0068b7"

            g <- ggplot(df, aes(x={x_data_name}, y={y_data_name}))


            g <- g +
            geom_point(colour = cLightBlue, size = 1)+
            theme_gray(base_family = "HiraKakuProN-W3")+
            xlab('{x_axis_name}')+
            ylab('{y_axis_name}')

            ggsave(file='{FilePath}', plot=g, width=10, height=5, device="cairo_ps")
        }}
    """.format(
            FilePath=PlotFilePath,
            x_axis_name=x_axis_name,
            y_axis_name=y_axis_name,
            x_data_name=x_data_name,
            y_data_name=y_data_name)

    plotFunc = robj.r(r_script)

    robj.pandas2ri.activate()
    testData_R = robj.conversion.py2ri(Data)

    plotFunc(testData_R)