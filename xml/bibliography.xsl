<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:math="http://www.w3.org/2005/xpath-functions/math"
    exclude-result-prefixes="xs math"
    version="3.0">
    
    <xsl:template match="/">
        <html>
            <head>
                <title>Bibliography - Graydon Kupfer's Schreyer Honors Project: Everyday</title>
                <link rel="stylesheet" type="text/css" href="HPstyle.css" />
            </head>
            <body>
                <h1>Graydon Kupfer's Schreyer Honors Project: Everyday</h1>
                <nav><p style="color:blue"><a href="index.html"><strong>Home</strong></a> | <a href="bibOutput.html"><strong>Bibliography</strong></a> | <a href="about.html"><strong>About</strong></a></p></nav>
                
                <xsl:apply-templates/>
                <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.
            </body>
            
        </html>
    </xsl:template>
    
    <xsl:template match="head">
        <h2>
            <xsl:apply-templates/>
        </h2>
    </xsl:template>
    
    <xsl:template match="note">
        <h3>
        <xsl:apply-templates/>
        </h3>
    </xsl:template>
    
    <xsl:template match="title">
        <a>
        <h4>
            <xsl:apply-templates/>
        </h4>
        </a>
    </xsl:template>
    
    <xsl:template match="dev">
        <p>Developer:
            <xsl:apply-templates/>
        </p>
    </xsl:template>
    
    <xsl:template match="pub">
        <p>Publisher:
            <xsl:apply-templates/>
        </p>
    </xsl:template>
    
    <xsl:template match="author">
        <p>Author:
            <xsl:apply-templates/>
        </p>
    </xsl:template>
    
    <!--<xsl:template match="a">
        <a>Link
            <xsl:apply-templates/>
        </a>
    </xsl:template>-->
    
    <xsl:template match="link">
        <p>
            <xsl:apply-templates select="descendant::link"/>
        </p>
    </xsl:template>
    
</xsl:stylesheet>