


def ie_template(batch_rows):
    template = """
    <?xml version="1.0" encoding="UTF-8"?>
<mets:mets xmlns:mets="http://www.loc.gov/METS/">
  <mets:dmdSec ID="ie-dmd">
    <mets:mdWrap MDTYPE="DC">
      <mets:xmlData>
        <dc:record xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
            <dc:title>""" + batch_rows[0]['title'] + """</dc:title>
              <dc:identifier>""" + batch_rows[0]['ark'] + """</dc:identifier>
              <dc:relation>""" + batch_rows[0]['relation'] + """</dc:relation>
              <dc:publisher>""" + batch_rows[0]['publisher'] + """</dc:publisher>
              <dc:creator>""" + batch_rows[0]['creator'] + """</dc:creator>
              <dc:date>""" + batch_rows[0]['date'] + """</dc:date>
              <dc:subject>""" + batch_rows[0]['subject'] + """</dc:subject>
            <dc:rights>""" + batch_rows[0]['rights'] + """</dc:rights>
              <dc:description>""" + batch_rows[0]['description'] + """</dc:description>
            <dc:ispartof>""" + batch_rows[0]['ispartof'] + """</dc:ispartof>
        </dc:record>
      </mets:xmlData>
    </mets:mdWrap>
  </mets:dmdSec>"""

    counter = 0
    for row in batch_rows:
        counter += 1
        template += inner_template_mets_amdsec(row, counter)

    template += """
  <mets:amdSec ID="rep1-amd">
    <mets:techMD ID="rep1-amd-tech">
      <mets:mdWrap MDTYPE="OTHER" OTHERMDTYPE="dnx">
        <mets:xmlData>
          <dnx xmlns="http://www.exlibrisgroup.com/dps/dnx">
            <section id="generalRepCharacteristics">
              <record>
                <key id="preservationType">PRESERVATION_MASTER</key>
                <key id="usageType">VIEW</key>
                <key id="RevisionNumber">1</key>
                <key id="DigitalOriginal">false</key>
              </record>
            </section>
          </dnx>
        </mets:xmlData>
      </mets:mdWrap>
    </mets:techMD>
    <mets:rightsMD ID="rep1-amd-rights">
      <mets:mdWrap MDTYPE="OTHER" OTHERMDTYPE="dnx">
        <mets:xmlData>
          <dnx xmlns="http://www.exlibrisgroup.com/dps/dnx"/>
        </mets:xmlData>
      </mets:mdWrap>
    </mets:rightsMD>
    <mets:sourceMD ID="rep1-amd-source">
      <mets:mdWrap MDTYPE="OTHER" OTHERMDTYPE="dnx">
        <mets:xmlData>
          <dnx xmlns="http://www.exlibrisgroup.com/dps/dnx"/>
        </mets:xmlData>
      </mets:mdWrap>
    </mets:sourceMD>
    <mets:digiprovMD ID="rep1-amd-digiprov">
      <mets:mdWrap MDTYPE="OTHER" OTHERMDTYPE="dnx">
        <mets:xmlData>
          <dnx xmlns="http://www.exlibrisgroup.com/dps/dnx"/>
        </mets:xmlData>
      </mets:mdWrap>
    </mets:digiprovMD>
  </mets:amdSec>
  <mets:amdSec ID="ie-amd">
    <mets:techMD ID="ie-amd-tech">
      <mets:mdWrap MDTYPE="OTHER" OTHERMDTYPE="dnx">
        <mets:xmlData>
          <dnx xmlns="http://www.exlibrisgroup.com/dps/dnx"/>
        </mets:xmlData>
      </mets:mdWrap>
    </mets:techMD>
    <mets:rightsMD ID="ie-amd-rights">
      <mets:mdWrap MDTYPE="OTHER" OTHERMDTYPE="dnx">
        <mets:xmlData>
          <dnx xmlns="http://www.exlibrisgroup.com/dps/dnx"/>
        </mets:xmlData>
      </mets:mdWrap>
    </mets:rightsMD>
    <mets:sourceMD ID="ie-amd-source">
      <mets:mdWrap MDTYPE="OTHER" OTHERMDTYPE="dnx">
        <mets:xmlData>
          <dnx xmlns="http://www.exlibrisgroup.com/dps/dnx"/>
        </mets:xmlData>
      </mets:mdWrap>
    </mets:sourceMD>
    <mets:digiprovMD ID="ie-amd-digiprov">
      <mets:mdWrap MDTYPE="OTHER" OTHERMDTYPE="dnx">
        <mets:xmlData>
          <dnx xmlns="http://www.exlibrisgroup.com/dps/dnx"/>
        </mets:xmlData>
      </mets:mdWrap>
    </mets:digiprovMD>
  </mets:amdSec>
  <mets:fileSec>
    <mets:fileGrp USE="VIEW" ID="rep1" ADMID="rep1-amd">"""

    counter = 0
    for row in batch_rows:
        counter += 1
        template += inner_template_file_sec(row, counter)

    template += """
    </mets:fileGrp>
  </mets:fileSec>
  <mets:structMap ID="rep1-1" TYPE="LOGICAL">
    <mets:div LABEL="PRESERVATION_MASTER;VIEW">
      <mets:div LABEL="Table of Contents">"""

    counter = 0
    for row in batch_rows:
        counter += 1
        template += inner_template_mets_div(row, counter)

    template += """
      </mets:div>
    </mets:div>
  </mets:structMap>
</mets:mets>
    """
    return template.strip()


def inner_template_mets_div(row, counter):
    template = """        <mets:div LABEL=""" + row['filename'] + """ TYPE="FILE">
          <mets:fptr FILEID="fid""" + str(counter) + """-1"/>
        </mets:div>"""
    return template


def inner_template_mets_amdsec(row, counter):
    template = """
      <mets:amdSec ID="fid""" + str(counter) + """-1-amd">
    <mets:techMD ID="fid""" + str(counter) + """-1-amd-tech">
      <mets:mdWrap MDTYPE="OTHER" OTHERMDTYPE="dnx">
        <mets:xmlData>
          <dnx xmlns="http://www.exlibrisgroup.com/dps/dnx">
            <section id="generalFileCharacteristics">
              <record>
                <key id="label">""" + row['ark'] + "." + row['filename'] + """</key>
              </record>
            </section>
            <section id="fileFixity">
              <record>
                <key id="fixityType">SHA1</key>
                <key id="fixityValue">""" + row['sha1'] + """</key>
              </record>
            </section>
          </dnx>
        </mets:xmlData>
      </mets:mdWrap>
    </mets:techMD>
    <mets:rightsMD ID="fid""" + str(counter) + """-1-amd-rights">
      <mets:mdWrap MDTYPE="OTHER" OTHERMDTYPE="dnx">
        <mets:xmlData>
          <dnx xmlns="http://www.exlibrisgroup.com/dps/dnx"/>
        </mets:xmlData>
      </mets:mdWrap>
    </mets:rightsMD>
    <mets:sourceMD ID="fid""" + str(counter) + """-1-amd-source">
      <mets:mdWrap MDTYPE="OTHER" OTHERMDTYPE="dnx">
        <mets:xmlData>
          <dnx xmlns="http://www.exlibrisgroup.com/dps/dnx"/>
        </mets:xmlData>
      </mets:mdWrap>
    </mets:sourceMD>
    <mets:digiprovMD ID="fid""" + str(counter) + """-1-amd-digiprov">
      <mets:mdWrap MDTYPE="OTHER" OTHERMDTYPE="dnx">
        <mets:xmlData>
          <dnx xmlns="http://www.exlibrisgroup.com/dps/dnx"/>
        </mets:xmlData>
      </mets:mdWrap>
    </mets:digiprovMD>
  </mets:amdSec>
    """
    return template.strip()

def inner_template_file_sec(row, counter):
    template = """
      <mets:file ID="fid""" + str(counter) + """-1" MIMETYPE="image/jpeg" ADMID="fid""" + str(counter) + """-1-amd">
        <mets:FLocat xlin:href="file://""" + row['filename'] + """" xmlns:xlin="http://www.w3.org/1999/xlink" LOCTYPE="URL"/>
      </mets:file>"""
    return template.strip()

def dc_template(row):
    template_string = """
<?xml version="1.0" encoding="UTF-8"?>
<record xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dc:title>""" + row[0]['title'] + """</dc:title>
  <dc:identifier>""" + row[0]['ark'] + """</dc:identifier>
  <dc:relation>""" + row[0]['relation'] + """</dc:relation>
  <dc:publisher>""" + row[0]['publisher'] + """</dc:publisher>
  <dc:creator>""" + row[0]['creator'] + """</dc:creator>
  <dc:date>""" + row[0]['date'] + """</dc:date>
  <dc:subject>""" + row[0]['subject'] + """</dc:subject>
  <dc:rights>""" + row[0]['rights'] + """</dc:rights>
  <dc:description>""" + row[0]['description'] + """</dc:description>
  <dc:ispartof>""" + row[0]['ispartof'] + """</dc:ispartof>
</record>
    """
    return template_string.strip()