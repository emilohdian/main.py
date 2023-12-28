import sys
from pathlib import Path

jpeg_files = list()
png_files = list()
jpg_files = list()
txt_files = list()
docx_files = list()
svg_files = list()
avi_files = list()
mp4_files = list()
mov_files = list()
mkv_files = list()
doc_files = list()
pdf_files = list()
xlsx_files = list()
pptx_files = list()
mp3_files = list()
ogg_files = list()
wav_files = list()
amr_files = list()
folders = list()
archives = list()
others = list()
unknown = set()
extensions = set()

registered_extensions = {
    'JPEG': jpeg_files,
    'PNG': png_files,
    'JPG': jpg_files,
    'TXT': txt_files,
    'DOCX': docx_files,
    'ZIP': archives,
    'SVG': svg_files,
    'AVI': avi_files,
    'MP4': mp4_files,
    'MOV': mov_files,
    'MKV': mkv_files,
    'DOC': doc_files,
    'PDF': pdf_files,
    'XLSX': xlsx_files,
    'PPTX': pptx_files,
    'MP3': mp3_files,
    'OGG': ogg_files,
    'WAV': wav_files,
    'AMR': amr_files
}

def get_extensions(file_name):
    return Path(file_name).suffix[1:].upper()

def scan(folder):
    for item in folder.iterdir():
        if item.is_dir():
            if item.name not in ('JPEG', 'PNG', 'JPG', 'TXT', 'DOCX', 'ARCHIVE', 'OTHER'):
                folders.append(item)
                scan(item)
            continue

        extension = get_extensions(file_name=item.name)
        new_name = folder/item.name
        if not extension:
            others.append(new_name)
        else:
            try:
                container = registered_extensions[extension]
                extensions.add(extension)
                container.append(new_name)
            except KeyError:
                unknown.add(extension)
                others.append(new_name)

if __name__ == '__main__':
    path = sys.argv[1]
    print(f"Start in {path}")

    folder = Path(path)

    scan(folder)

    print(f"jpeg: {jpeg_files}")
    print(f"jpg: {jpg_files}")
    print(f"png: {png_files}")
    print(f"txt: {txt_files}")
    print(f"docx: {docx_files}")
    print(f"svg: {svg_files}")
    print(f"avi: {avi_files}")
    print(f"mp4: {mp4_files}")
    print(f"mov: {mov_files}")
    print(f"mkv: {mkv_files}")
    print(f"doc: {doc_files}")
    print(f"pdf: {pdf_files}")
    print(f"xlsx: {xlsx_files}")
    print(f"pptx: {pptx_files}")
    print(f"mp3: {mp3_files}")
    print(f"ogg: {ogg_files}")
    print(f"wav: {wav_files}")
    print(f"amr: {amr_files}")
    print(f"archive: {archives}")
    print(f"unkown: {others}")
    print(f"All extensions: {extensions}")
    print(f"Unknown extensions: {unknown}")
    print(f"Folder: {folders}")
