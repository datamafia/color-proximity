# color-proximity
Calculate color proximity using Python as a translation from https://github.com/gausie/colour-proximity

### Version 1.0

Written using Python 2.7

### Tests

Simply run ```python tests.py``` in the terminal.

### Example

```
#!/usr/bin/env python

from color_proximity import color_proximity

cp = color_proximity()

res = cp.proximity((255,255,255), (255,000,255))
# tuple or list accepted. 
# Type can be mixed. 
# Alpha channel ignored if present.
```

#### References

Translated from https://github.com/gausie/colour-proximity into Python. Original file included for reference.

Also interesting http://www.easyrgb.com/index.php?X=MATH

[datamafia](http://datamafia.com) [github/datamaifa](http://github.com/datamafia)

##### License 

Dual licensed under GPL and BSD

__GPL :__ [GPL license info via gnu.org](http://www.gnu.org/licenses/)

Color proximity calculation using Python
Copyright (C) 2015  Data Mafia

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see http://www.gnu.org/licenses/.

__BSD :__ [BSD license info via OpenSource.org](http://opensource.org/licenses/BSD-3-Clause)

Copyright (c) 2014, Data Mafia
All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
