def fill_template(r):
    template = """
    <?xml version="1.0" encoding="UTF-8"?>
<mets:mets xmlns:mets="http://www.loc.gov/METS/">
  <mets:dmdSec ID="ie-dmd">
    <mets:mdWrap MDTYPE="DC">
      <mets:xmlData>
        <dc:record xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
            <dc:title>""" + r['title'] + """</dc:title>
  <dc:identifier>""" + r['ark'] + """</dc:identifier>
  <dc:relation>""" + r['relation'] + """</dc:relation>
  <dc:publisher>""" + r['publisher'] + """</dc:publisher>
  <dc:creator>""" + r['creator'] + """</dc:creator>
  <dc:date>""" + r['date'] + """</dc:date>
  <dc:subject>""" + r['subject'] + """</dc:subject>
<dc:rights>""" + r['rights'] + """</dc:rights>
  <dc:description>""" + r['description'] + """</dc:description>
<dc:ispartof>""" + r['ispartof'] + """</dc:ispartof>
        </dc:record>
      </mets:xmlData>
    </mets:mdWrap>
  </mets:dmdSec>
  <mets:amdSec ID="fid1-1-amd">
    <mets:techMD ID="fid1-1-amd-tech">
      <mets:mdWrap MDTYPE="OTHER" OTHERMDTYPE="dnx">
        <mets:xmlData>
          <dnx xmlns="http://www.exlibrisgroup.com/dps/dnx">
            <section id="generalFileCharacteristics">
              <record>
                <key id="label">""" + r['ark'] + "." + r['filename'] + """</key>
              </record>
            </section>
            <section id="fileFixity">
              <record>
                <key id="fixityType">SHA1</key>
                <key id="fixityValue">""" + r['sha1'] + """</key>
              </record>
            </section>
          </dnx>
        </mets:xmlData>
      </mets:mdWrap>
    </mets:techMD>
    <mets:rightsMD ID="fid1-1-amd-rights">
      <mets:mdWrap MDTYPE="OTHER" OTHERMDTYPE="dnx">
        <mets:xmlData>
          <dnx xmlns="http://www.exlibrisgroup.com/dps/dnx"/>
        </mets:xmlData>
      </mets:mdWrap>
    </mets:rightsMD>
    <mets:sourceMD ID="fid1-1-amd-source">
      <mets:mdWrap MDTYPE="OTHER" OTHERMDTYPE="dnx">
        <mets:xmlData>
          <dnx xmlns="http://www.exlibrisgroup.com/dps/dnx"/>
        </mets:xmlData>
      </mets:mdWrap>
    </mets:sourceMD>
    <mets:digiprovMD ID="fid1-1-amd-digiprov">
      <mets:mdWrap MDTYPE="OTHER" OTHERMDTYPE="dnx">
        <mets:xmlData>
          <dnx xmlns="http://www.exlibrisgroup.com/dps/dnx"/>
        </mets:xmlData>
      </mets:mdWrap>
    </mets:digiprovMD>
  </mets:amdSec>
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
    <mets:fileGrp USE="VIEW" ID="rep1" ADMID="rep1-amd">
      <mets:file ID="fid1-1" MIMETYPE="image/jpeg" ADMID="fid1-1-amd">
        <mets:FLocat xlin:href="file://""" + r['filename'] + """" xmlns:xlin="http://www.w3.org/1999/xlink" LOCTYPE="URL"/>
      </mets:file>
    </mets:fileGrp>
  </mets:fileSec>
  <mets:structMap ID="rep1-1" TYPE="LOGICAL">
    <mets:div LABEL="PRESERVATION_MASTER;VIEW">
      <mets:div LABEL="Table of Contents">
        <mets:div LABEL=""" + r['filename'] + """ TYPE="FILE">
          <mets:fptr FILEID="fid1-1"/>
        </mets:div>
      </mets:div>
    </mets:div>
  </mets:structMap>
</mets:mets>
    """
    return template.strip()

def dc_template(row):
    template_string = """
    <?xml version="1.0" encoding="UTF-8"?>
<record xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dc:title>""" + row['title'] + """</dc:title>
  <dc:identifier>""" + row['ark'] + """</dc:identifier>
  <dc:relation>""" + row['relation'] + """</dc:relation>
  <dc:publisher>""" + row['publisher'] + """</dc:publisher>
  <dc:creator>""" + row['creator'] + """</dc:creator>
  <dc:date>""" + row['date'] + """</dc:date>
  <dc:subject>""" + row['subject'] + """</dc:subject>
<dc:rights>""" + row['rights'] + """</dc:rights>
  <dc:description>""" + row['description'] + """</dc:description>
<dc:ispartof>""" + row['ispartof'] + """</dc:ispartof>
</record>
    """
    return template_string.strip()