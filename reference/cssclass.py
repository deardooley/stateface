#!/usr/bin/env python
"""
Generates CSS rules for StateFace using state abbreviations rather than codes.

Pass it the .json file containing the mapping between state abbrevations
and StateFace code letters.
"""
from string import Template
import sys

try:
    import json
except ImportError:
    import simplejson as json

CLASS_PREFIX = 'stateface'
FONT_NAME = 'StateFaceRegular'

CSS = Template("""\
@font-face {
  font-family: '$fontname';
  src: url('../font/webfont/$prefix-regular-webfont.eot');
  src: url('../font/webfont/$prefix-regular-webfont.eot?#iefix') format('embedded-opentype'),
  url('../font/webfont/$prefix-regular-webfont.woff') format('woff'),
  url('../font/webfont/$prefix-regular-webfont.ttf') format('truetype'),
  url('../font/webfont/$prefix-regular-webfont.svg#$fontname') format('svg');
  font-weight: normal;
  font-style: normal;
}
.$prefix {
  display: inline-block;
  font: normal normal normal 14px/1 $fontname;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
/* makes the font 33% larger relative to the icon container */
.$prefix-lg {
  font-size: 1.33333333em;
  line-height: 0.75em;
  vertical-align: -15%;
}
.$prefix-2x {
  font-size: 2em;
}
.$prefix-3x {
  font-size: 3em;
}
.$prefix-4x {
  font-size: 4em;
}
.$prefix-5x {
  font-size: 5em;
}
.$prefix-fw {
  width: 1.28571429em;
  text-align: center;
}
.$prefix-ul {
  padding-left: 0;
  margin-left: 2.14285714em;
  list-style-type: none;
}
.$prefix-ul > li {
  position: relative;
}
.$prefix-li {
  position: absolute;
  left: -2.14285714em;
  width: 2.14285714em;
  top: 0.14285714em;
  text-align: center;
}
.stateface-li.stateface-lg {
  left: -1.85714286em;
}
.$prefix-border {
  padding: .2em .25em .15em;
  border: solid 0.08em #eeeeee;
  border-radius: .1em;
}
.$prefix.pull-left {
  margin-right: .3em;
}
.$prefix.pull-right {
  margin-left: .3em;
}
.$prefix-spin {
  -webkit-animation: fa-spin 2s infinite linear;
  animation: fa-spin 2s infinite linear;
}
@-webkit-keyframes $prefix-spin {
  0% {
    -webkit-transform: rotate(0deg);
    transform: rotate(0deg);
  }
  100% {
    -webkit-transform: rotate(359deg);
    transform: rotate(359deg);
  }
}
@keyframes $prefix-spin {
  0% {
    -webkit-transform: rotate(0deg);
    transform: rotate(0deg);
  }
  100% {
    -webkit-transform: rotate(359deg);
    transform: rotate(359deg);
  }
}
.$prefix-rotate-90 {
  filter: progid:DXImageTransform.Microsoft.BasicImage(rotation=1);
  -webkit-transform: rotate(90deg);
  -ms-transform: rotate(90deg);
  transform: rotate(90deg);
}
.$prefix-rotate-180 {
  filter: progid:DXImageTransform.Microsoft.BasicImage(rotation=2);
  -webkit-transform: rotate(180deg);
  -ms-transform: rotate(180deg);
  transform: rotate(180deg);
}
.$prefix-rotate-270 {
  filter: progid:DXImageTransform.Microsoft.BasicImage(rotation=3);
  -webkit-transform: rotate(270deg);
  -ms-transform: rotate(270deg);
  transform: rotate(270deg);
}
.$prefix-flip-horizontal {
  filter: progid:DXImageTransform.Microsoft.BasicImage(rotation=0, mirror=1);
  -webkit-transform: scale(-1, 1);
  -ms-transform: scale(-1, 1);
  transform: scale(-1, 1);
}
.$prefix-flip-vertical {
  filter: progid:DXImageTransform.Microsoft.BasicImage(rotation=2, mirror=1);
  -webkit-transform: scale(1, -1);
  -ms-transform: scale(1, -1);
  transform: scale(1, -1);
}
:root .$prefix-rotate-90,
:root .$prefix-rotate-180,
:root .$prefix-rotate-270,
:root .$prefix-flip-horizontal,
:root .$prefix-flip-vertical {
  filter: none;
}
.$prefix-stack {
  position: relative;
  display: inline-block;
  width: 2em;
  height: 2em;
  line-height: 2em;
  vertical-align: middle;
}
.$prefix-stack-1x,
.$prefix-stack-2x {
  position: absolute;
  left: 0;
  width: 100%;
  text-align: center;
}
.$prefix-stack-1x {
  line-height: inherit;
}
.$prefix-stack-2x {
  font-size: 2em;
}
.$prefix-inverse {
  color: #ffffff;
}
""").substitute(prefix=CLASS_PREFIX).substitute(fontname=FONT_NAME)

STATE_RULE = Template("""\
.$prefix-$abbrev:before {
    content: "$code";
}
""").safe_substitute(prefix=CLASS_PREFIX)

def make_state_rules(state_mapping):
    rules = []

    for abbrev, code in sorted(state_mapping.iteritems()):
        rule = Template(STATE_RULE).substitute(
            abbrev=abbrev.lower(),
            code=code
        )
        rules.append(rule)

    return '\n'.join(rules)

def main():
    try:
        f = open(sys.argv[1])
    except IndexError:
        f = sys.stdin
    state_mapping = json.load(f)
    print CSS
    print make_state_rules(state_mapping)

if __name__ == '__main__':
    sys.exit(main())
