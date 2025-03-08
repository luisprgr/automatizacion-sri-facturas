from pathlib import Path
from typing import Annotated, TypeAlias

import typer

DatosOption: TypeAlias = Annotated[
    Path,
    typer.Option(
        "--datos",
        "-d",
        help=(
            "Archivo que contiene los datos de la factura y la información del "
            "remitente de la misma (ver README.md)."
        ),
    ),
]

HeadlessOption: TypeAlias = Annotated[
    bool,
    typer.Option(
        "--headless",
        "-h",
        help="Ejecuta el script sin mostrar las acciones en la ventana del navegador.",
    ),
]

GuardarCapturasOption: TypeAlias = Annotated[
    bool,
    typer.Option(
        "--guardar-capturas/--no-capturas",
        "-c/-n",
        help=(
            "Permite seleccionar si se deben guardar capturas de los formularios "
            "completados (login con contraseña censurada y los datos de la factura)."
        ),
    ),
]

TestOption: TypeAlias = Annotated[
    bool,
    typer.Option(
        "--test",
        "-t",
        help=(
            "Detiene el script tras completar los datos de la factura, permitiendo su "
            "revisión manual antes de guardarla como borrador o enviarla. "
            "Esta opción es ideal para verificar que la factura se llena correctamente."
        ),
    ),
]

FirmarOption: TypeAlias = Annotated[
    bool,
    typer.Option(
        "--firmar-y-enviar",
        "-e",
        help=(
            "Indica al programa que firme y envíe la factura automáticamente una vez esta "
            "sea llenada, ideal para enviar una factura automáticamente con el script tras "
            "verificar que se está llenando correctamente con --test."
        ),
    ),
]
