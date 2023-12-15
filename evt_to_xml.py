import Evtx.Evtx as evtx
import Evtx.Views as e_views
import os
import datetime

def main():
    import argparse

    parser = argparse.ArgumentParser(
        description="Dump a binary EVTX file into XML.")
    parser.add_argument("evtx", type=str,
                        help="Path to the Windows EVTX event log file")
    args = parser.parse_args()

    with evtx.Evtx(args.evtx) as log:
        output_file = args.evtx.replace(".evtx", ".xml")
        print(f"outputting to {output_file}")
        try:
            os.remove(output_file)
        except FileNotFoundError:
            pass
        with open(output_file, mode="w") as file:
            file.write(e_views.XML_HEADER)
            file.write("<Events>")
            cnt = 0
            fup_cnt = 0
            for record in log.records():
                cnt += 1
                if cnt % 10000 == 0:
                    print(f"{str(datetime.datetime.now())} {cnt}")
                try:
                    out_xml = record.xml()
                    file.write(out_xml + "\n")
                    # print(out_xml)
                except UnicodeDecodeError:
                    file.write("<FuckedUpRecordDeleted />\n")
                    fup_cnt += 1
                    print(f"fucked up: {cnt}, total: {fup_cnt}")
            file.write("</Events>")


if __name__ == "__main__":
    main()