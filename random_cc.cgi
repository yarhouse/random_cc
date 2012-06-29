#!/usr/bin/ruby

require 'cgi'

t = Time.new
st = t.utc - 25200

# End result can't have both Sexy and Cute
sexy_cute = ['Sexy', 'Cute'].shuffle

# End result can't have both Scary and Intimidating
scar_intim = ['Scary', 'Intimidating'].shuffle

# Take other catagories and the first of the last 2
others = (['Retro', 'Elemental', 'Tech', 'Fantasy', 'Creature', 'Oddball'] << sexy_cute.first << scar_intim.first).shuffle

used = (others[0..4]).shuffle # Our 5 random cats
not_used = (others[5..8] << sexy_cute.last << scar_intim.last).shuffle # The leftovers

# A basic html output, also includes the current server time in game
# which is just PST, and a refresh button to reload the page for new cats
puts "Content-type:text/html\n\n
<!DOCTYPE html>
<html>
<body>
<b><font size=\"6\">S.P.E.A.R. Random CC Catagories</font></b><br />
<br />
<font size=\"4\">Champions Server Time is currently #{st.strftime("%l:%M %P")}</font><br />
<br />
Random catagories:<br />
<b>#{used.join(', ')}, and Best</b><br />
<br />
Not used:<br />
<b>#{not_used.join(', ')}</b><br />
<br />
<form><input type=\"button\" onClick=\"history.go(0)\" value=\"Refresh\"></form>
<br />
</body>
</html>"

# Used this to know what my shared host was running
if RUBY_PLATFORM =~ /win23/
	puts "We're in Windows"
elsif RUBY_PLATFORM =~ /linux/
	puts "We're in Linux"
elsif RUBY_PLATFORM =~ /darwin/
	puts "We're in Mac OS"
elsif RUBY_PLATFORM =~ /freebsd/
	puts "We're in FreeDSB"
else
	puts "This is an unknown system"
end