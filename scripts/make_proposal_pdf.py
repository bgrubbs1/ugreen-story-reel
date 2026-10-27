#!/usr/bin/env python3
"""Generate the Round 1 Project Proposal PDF for the story-reel skill.

Pure Python 3 standard library only. No PDF libraries are installed, so this
script writes a minimal, valid PDF 1.4 document directly: Helvetica text,
word-wrapped paragraphs, automatic pagination, and an xref table.

It also enforces the official 500-word cap for the ten substantive answers and
fails (exit 1) if the answers are over the limit.

Usage:
    python3 scripts/make_proposal_pdf.py            # build the PDF + report
    python3 scripts/make_proposal_pdf.py --check    # word-count check only

Source of truth: proposal/round1-proposal.md
Output:          proposal/round1-proposal.pdf
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "proposal" / "round1-proposal.md"
OUTPUT = ROOT / "proposal" / "round1-proposal.pdf"

WORD_LIMIT = 500
PAGE_W, PAGE_H = 612.0, 792.0      # US Letter, points
MARGIN_X, MARGIN_TOP, MARGIN_BOT = 72.0, 64.0, 68.0
BODY_SIZE, BODY_LEAD = 10.5, 14.5

# Helvetica AFM advance widths (units per 1000 em) for printable ASCII.
HELVETICA_WIDTHS = {
    " ": 278, "!": 278, '"': 355, "#": 556, "$": 556, "%": 889, "&": 667,
    "'": 191, "(": 333, ")": 333, "*": 389, "+": 584, ",": 278, "-": 333,
    ".": 278, "/": 278, ":": 278, ";": 278, "<": 584, "=": 584, ">": 584,
    "?": 556, "@": 1015, "[": 278, "\\": 278, "]": 278, "^": 469, "_": 556,
    "`": 333, "{": 334, "|": 260, "}": 334, "~": 584,
}
for _ch in "0123456789":
    HELVETICA_WIDTHS[_ch] = 556
for _ch, _w in zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                   [667, 667, 722, 722, 667, 611, 778, 722, 278, 500, 667,
                    556, 833, 722, 778, 667, 778, 722, 667, 611, 722, 667,
                    944, 667, 667, 611]):
    HELVETICA_WIDTHS[_ch] = _w
for _ch, _w in zip("abcdefghijklmnopqrstuvwxyz",
                   [556, 556, 500, 556, 556, 278, 556, 556, 222, 222, 500,
                    222, 833, 556, 556, 556, 556, 333, 500, 278, 556, 500,
                    722, 500, 500, 500]):
    HELVETICA_WIDTHS[_ch] = _w


def text_width(text, size, bold=False):
    units = sum(HELVETICA_WIDTHS.get(ch, 556) for ch in text)
    width = units * size / 1000.0
    return width * 1.04 if bold else width


def wrap(text, size, max_width, bold=False):
    """Word-wrap a paragraph into lines that fit max_width points."""
    words = text.split()
    lines, current = [], ""
    for word in words:
        candidate = word if not current else current + " " + word
        if text_width(candidate, size, bold) <= max_width:
            current = candidate
            continue
        if current:
            lines.append(current)
        # A single word wider than the column is broken by characters.
        while text_width(word, size, bold) > max_width:
            cut = len(word)
            while cut > 1 and text_width(word[:cut], size, bold) > max_width:
                cut -= 1
            lines.append(word[:cut])
            word = word[cut:]
        current = word
    if current:
        lines.append(current)
    return lines


def pdf_escape(text):
    return text.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")


def count_words(text):
    """Count English words: whitespace tokens that contain a letter or digit."""
    return sum(1 for token in text.split() if re.search(r"[A-Za-z0-9]", token))


def strip_inline_markdown(text):
    text = text.replace("**", "").replace("__", "")
    text = text.replace("`", "")
    return text.strip()


def extract_answers(source):
    start_marker = "<!-- WORDCOUNT-START -->"
    end_marker = "<!-- WORDCOUNT-END -->"
    if start_marker not in source or end_marker not in source:
        raise SystemExit("word-count markers missing in proposal source")
    block = source.split(start_marker, 1)[1].split(end_marker, 1)[0]
    answer_lines = [
        line for line in block.splitlines()
        if line.strip() and not line.lstrip().startswith("#")
    ]
    answers = strip_inline_markdown("\n".join(answer_lines))
    if not answers:
        raise SystemExit("no answers found between the word-count markers")
    return answers, count_words(answers)


class Page:
    def __init__(self):
        self.content = []

    def add(self, command):
        self.content.append(command)


class PdfWriter:
    def __init__(self):
        self.pages = []
        self.y = PAGE_H - MARGIN_TOP
        self.new_page()

    # ---------- low-level drawing ----------
    def new_page(self):
        self.page = Page()
        self.pages.append(self.page)
        self.y = PAGE_H - MARGIN_TOP

    def ensure(self, needed):
        if self.y - needed < MARGIN_BOT:
            self.new_page()

    def draw(self, x, y, text, font, size, rgb):
        if not text:
            return
        command = (
            "BT\n%.3f %.3f %.3f rg\n/%s %.2f Tf\n1 0 0 1 %.2f %.2f Tm\n(%s) Tj\nET\n"
            % (rgb[0], rgb[1], rgb[2], font, size, x, y, pdf_escape(text))
        )
        self.page.add(command)

    def line(self, x1, y1, x2, y2, rgb, width=0.75):
        self.page.add(
            "%.3f %.3f %.3f RG\n%.2f w\n%.2f %.2f m %.2f %.2f l S\n"
            % (rgb[0], rgb[1], rgb[2], width, x1, y1, x2, y2)
        )

    # ---------- block layout ----------
    def heading(self, text, size, rgb, before, after):
        self.ensure(before + size + after)
        self.y -= before
        self.draw(MARGIN_X, self.y - size, text, "F2", size, rgb)
        self.y -= size + after

    def wrapped_heading(self, text, size, rgb, before, after):
        """Bold heading that wraps instead of overflowing the text column."""
        lines = wrap(text, size, PAGE_W - 2 * MARGIN_X, bold=True)
        leading = size * 1.24
        self.ensure(before + leading * len(lines) + after)
        self.y -= before
        for line in lines:
            self.draw(MARGIN_X, self.y - size, line, "F2", size, rgb)
            self.y -= leading
        self.y -= after

    def paragraph(self, text, size=BODY_SIZE, lead=BODY_LEAD, rgb=(0.09, 0.09, 0.12),
                  indent=0.0, bold=False):
        font = "F2" if bold else "F1"
        lines = wrap(text, size, PAGE_W - 2 * MARGIN_X - indent, bold=bold)
        for line in lines:
            self.ensure(lead)
            self.draw(MARGIN_X + indent, self.y - size, line, font, size, rgb)
            self.y -= lead

    def bullet(self, text):
        size, lead, indent = BODY_SIZE, BODY_LEAD, 14.0
        lines = wrap(text, size, PAGE_W - 2 * MARGIN_X - indent)
        # Keep short bullets intact: move the whole bullet to the next page if
        # it would otherwise be split across pages.
        if self.page.content and self.y - lead * len(lines) < MARGIN_BOT:
            self.new_page()
        for index, line in enumerate(lines):
            self.ensure(lead)
            if index == 0:
                self.draw(MARGIN_X, self.y - size, "-", "F1", size, (0.09, 0.09, 0.12))
            self.draw(MARGIN_X + indent, self.y - size, line, "F1", size, (0.09, 0.09, 0.12))
            self.y -= lead

    def gap(self, points):
        self.y -= points

    # ---------- document assembly ----------
    def render(self, markdown, word_count):
        navy = (0.10, 0.22, 0.36)
        grey = (0.38, 0.38, 0.42)
        ink = (0.09, 0.09, 0.12)

        lines = markdown.splitlines()
        first_block = True
        for raw in lines:
            line = raw.rstrip()
            stripped = line.strip()
            if not stripped or stripped.startswith("<!--"):
                continue
            if stripped.startswith("# "):
                title = strip_inline_markdown(stripped[2:])
                self.wrapped_heading(title, 17.5, navy, before=0, after=5)
                continue
            if stripped.startswith("## "):
                heading = strip_inline_markdown(stripped[3:])
                self.gap(6)
                self.wrapped_heading(heading, 12.5, navy, before=8, after=9)
                continue
            if stripped.startswith("### "):
                heading = strip_inline_markdown(stripped[4:])
                self.gap(2)
                self.wrapped_heading(heading, 10.8, ink, before=7, after=5)
                continue
            if stripped.startswith("- "):
                self.bullet(strip_inline_markdown(stripped[2:]))
                continue
            text = strip_inline_markdown(stripped)
            if first_block:
                # Subtitle lines directly under the title.
                self.paragraph(text, size=9.6, lead=12.5, rgb=grey)
                first_block = False
                continue
            if "WORDCOUNT_VALUE" in text:
                text = text.replace("WORDCOUNT_VALUE", str(word_count))
                self.paragraph(text, size=9.4, lead=12.4, rgb=grey)
                self.gap(2)
                self.line(MARGIN_X, self.y + 6, PAGE_W - MARGIN_X, self.y + 6, (0.75, 0.78, 0.82), 0.6)
                self.gap(4)
                continue
            self.paragraph(text)
            self.gap(1.5)

        total = len(self.pages)
        for index, page in enumerate(self.pages, start=1):
            footer = "Story Reel | Round 1 Project Proposal | page %d of %d" % (index, total)
            page.content.append(
                "0.55 0.55 0.58 rg\nBT\n/F1 8.5 Tf\n1 0 0 1 %.2f 34 Tm\n(%s) Tj\nET\n"
                % (MARGIN_X, pdf_escape(footer))
            )
        return self.pages

    def build(self):
        pages = self.pages
        page_count = len(pages)
        objects = {}
        page_ids, content_ids = [], []
        next_id = 6
        for _ in pages:
            page_ids.append(next_id)
            content_ids.append(next_id + 1)
            next_id += 2
        info_id = next_id

        objects[1] = "<< /Type /Catalog /Pages 2 0 R >>"
        kids = " ".join("%d 0 R" % pid for pid in page_ids)
        objects[2] = "<< /Type /Pages /Kids [%s] /Count %d >>" % (kids, page_count)
        objects[3] = "<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica /Encoding /WinAnsiEncoding >>"
        objects[4] = "<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold /Encoding /WinAnsiEncoding >>"
        objects[5] = "<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Oblique /Encoding /WinAnsiEncoding >>"
        objects[info_id] = (
            "<< /Title (Story Reel - Round 1 Project Proposal) "
            "/Subject (UGREEN Hackathon 2026 on AI NAS - Bring Memories to Life) "
            "/Creator (scripts/make_proposal_pdf.py) >>"
        )
        for index, page in enumerate(pages):
            stream = "".join(page.content).encode("latin-1")
            objects[page_ids[index]] = (
                "<< /Type /Page /Parent 2 0 R /MediaBox [0 0 %.0f %.0f] "
                "/Resources << /Font << /F1 3 0 R /F2 4 0 R /F3 5 0 R >> >> "
                "/Contents %d 0 R >>" % (PAGE_W, PAGE_H, content_ids[index])
            )
            objects[content_ids[index]] = (
                "<< /Length %d >>\nstream\n" % len(stream)
            ).encode("latin-1") + stream + b"\nendstream"

        out = bytearray(b"%PDF-1.4\n%\xe2\xe3\xcf\xd3\n")
        offsets = {}
        for object_id in sorted(objects):
            offsets[object_id] = len(out)
            out += ("%d 0 obj\n" % object_id).encode("latin-1")
            body = objects[object_id]
            out += body if isinstance(body, bytes) else body.encode("latin-1")
            out += b"\nendobj\n"
        xref_offset = len(out)
        max_id = max(objects)
        out += ("xref\n0 %d\n" % (max_id + 1)).encode("latin-1")
        out += b"0000000000 65535 f \n"
        for object_id in range(1, max_id + 1):
            out += ("%010d 00000 n \n" % offsets[object_id]).encode("latin-1")
        out += (
            "trailer\n<< /Size %d /Root 1 0 R /Info %d 0 R >>\nstartxref\n%d\n%%%%EOF\n"
            % (max_id + 1, info_id, xref_offset)
        ).encode("latin-1")
        return bytes(out), page_count


def main():
    markdown = SOURCE.read_text(encoding="utf-8")
    answers, word_count = extract_answers(markdown)
    print("proposal source: %s" % SOURCE.relative_to(ROOT))
    print("ten answers: %d English words (limit %d)" % (word_count, WORD_LIMIT))
    if word_count > WORD_LIMIT:
        print("FAIL: the ten answers exceed the 500-word limit")
        return 1
    if "--check" in sys.argv:
        print("PASS: word count within the limit")
        return 0

    rendered = markdown.replace("WORDCOUNT_VALUE", str(word_count))
    try:
        rendered.encode("latin-1")
    except UnicodeEncodeError as error:
        print("FAIL: non Latin-1 character in proposal source: %r" % error.object[error.start:error.end])
        return 1

    writer = PdfWriter()
    writer.render(rendered, word_count)
    pdf_bytes, page_count = writer.build()
    OUTPUT.write_bytes(pdf_bytes)
    print("wrote: %s (%d bytes, %d pages)" % (OUTPUT.relative_to(ROOT), len(pdf_bytes), page_count))
    if len(pdf_bytes) > 1024 * 1024:
        print("FAIL: PDF exceeds the 1 MB Round 1 limit")
        return 1
    print("PASS: PDF built, word count within the limit, size within 1 MB")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
