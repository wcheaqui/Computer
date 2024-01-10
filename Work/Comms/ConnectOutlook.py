

import emlx
import glob

# for filepath in glob.iglob("/Users/WCheaq/Library/Mail/**/*.emlx", recursive=True):
#     m = emlx.read(filepath).headers
#     # print(m)
filepath = '/Users/WCheaq/Library/Mail/V10/79936577-8B98-4E44-9E97-BE66BB7516C3/Inbox.mbox/5817C326-5BD4-410F-8EB7-1114C7B0474C/Data/6/2/Messages/26605.emlx'
print(emlx.read(filepath).flags)
