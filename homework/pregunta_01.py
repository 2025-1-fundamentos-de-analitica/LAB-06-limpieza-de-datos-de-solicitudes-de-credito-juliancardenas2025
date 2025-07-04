"""
Escriba el codigo que ejecute la accion solicitada en la pregunta.
"""

import pandas as pd
import os
import glob

def pregunta_01():

    def cargar_datos(path): 
        return pd.read_csv(path, sep=";", index_col=0)

    def limpiar_columnas(df: pd.DataFrame):
        df["sexo"] = df["sexo"].str.strip().str.lower()
        df["tipo_de_emprendimiento"] = df["tipo_de_emprendimiento"].str.strip().str.lower()
        df["idea_negocio"] = df["idea_negocio"].str.strip().str.lower()
        df["idea_negocio"] = df["idea_negocio"].str.replace("á", "a").str.replace("é", "e").str.replace("í", "i").str.replace("ó", "o").str.replace("ú", "u")
        df["idea_negocio"] = df["idea_negocio"].str.replace(" ", "").str.translate(str.maketrans("", "", "-._"))
        df["barrio"] = df["barrio"].str.lower().str.replace("_", " ").str.replace("-", " ")
        df["comuna_ciudadano"] = df["comuna_ciudadano"].astype(int)
        df["fecha_de_beneficio"] = pd.to_datetime(df["fecha_de_beneficio"], dayfirst=True, format="mixed")
        df["monto_del_credito"] = df["monto_del_credito"].str.strip().str.strip("$").str.replace(".00", "").str.replace(",", "").astype(int)
        df["línea_credito"] = df["línea_credito"].str.strip().str.lower()
        df["línea_credito"] = df["línea_credito"].str.replace(" ", "")
        df["línea_credito"] = df["línea_credito"].str.translate(str.maketrans("", "", "-._"))
        return df

    def quitar_nulos_duplicados(df: pd.DataFrame): 
        return df.dropna().drop_duplicates()

    def guardar_datos(df:pd.DataFrame, path): 
        df.to_csv(path, index=False, sep=";")

    entrada = "files/input/solicitudes_de_credito.csv"
    salida = "files/output/solicitudes_de_credito.csv"
    if os.path.exists("files/output"):
        for f in glob.glob("files/output/*"): os.remove(f)
    else: os.makedirs("files/output")
    df = cargar_datos(entrada)
    df = limpiar_columnas(df)
    df = quitar_nulos_duplicados(df)
    guardar_datos(df, salida)
