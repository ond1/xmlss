<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="3.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template name="a">
        <xsl:result-document href="result-1.json" method="json">
            <xsl:sequence select='map { "value" : "foo" }'/>
        </xsl:result-document>
    </xsl:template>
</xsl:stylesheet>
