import typer

from ssg.site import Site


def main(souce='content', dest="dist"):
    config = {"source":source, "dest":dest}

    Site(**config).build()
 
typer.run(main)

