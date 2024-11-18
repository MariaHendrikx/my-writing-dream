# What is an Epub file behind the scenes?

When you rename an epub file to .zip, you can see a "behind the scenes" of an epub file. 
When looking inside, it might look like it's just some css and html, but ChatGPT told me it's a bit more than just these 2:

An EPUB file is a bit more complex than just a CSS file and an HTML file with paragraphs marked up as `<p>` elements. Here's a more accurate overview of what an EPUB file consists of:

1. **EPUB Container (ZIP Archive)**:
   - An EPUB file is essentially a compressed ZIP archive containing various files and directories.

2. **MIME Type**:
   - The root of the EPUB archive contains a file named `mimetype` which specifies the MIME type of the EPUB, typically `application/epub+zip`.

3. **META-INF Directory**:
   - This directory includes the `container.xml` file, which provides the location of the root file of the EPUB (usually an OPF file).

4. **Content Documents**:
   - These are XHTML files (similar to HTML but stricter in terms of XML syntax) which contain the text of the book. Each XHTML file may represent a chapter or section of the book. The content is marked up using standard XHTML tags, including `<p>` for paragraphs, but it can also include images, links, and other multimedia.

5. **CSS Files**:
   - EPUB files include CSS files to define the styling of the text and layout. These CSS files control the appearance of the XHTML content, such as fonts, colors, and spacing.

6. **OPF File (Package Document)**:
   - The OPF (Open Packaging Format) file is an XML file that contains metadata about the book (like title, author, and language), a manifest listing all the files in the EPUB, and a spine which indicates the reading order of the XHTML files.

7. **NCX File (Navigation Control)**:
   - The NCX file is used to define the table of contents and navigation structure for the EPUB. It provides a way for readers to jump to different parts of the book.

8. **Images and Other Media**:
   - EPUB files can include images, audio, video, and other media files referenced by the XHTML content.

In summary, while XHTML files within an EPUB use `<p>` tags for paragraphs, an EPUB is not just a simple combination of HTML and CSS. It is a structured format containing multiple components that together form a digital publication.