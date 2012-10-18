def coffee2js(coffee)
  r, w = IO.pipe
  system 'coffee', '-cbe', coffee, out: w
  w.close_write
  r.readlines.drop(1).join "\n"
end

params = ARGF.read.encode('UTF-8')
exit if params.length < 2

require 'cgi'
require 'json'
c = CGI.new
puts c.header
JSON.parse(params)['events'].each do |ev|
  text = ev['message']['text'][/\A!coffee (.*)/m, 1]
  puts coffee2js text if text
end
