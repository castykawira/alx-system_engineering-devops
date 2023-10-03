#!/usr/bin/env ruby
# This Ruby script processes TextMe app text messages transactions and outputs sender, receiver, and flags.
puts ARGV[0].scan(/\[from:(.*?)\]\s\[to:(.*?)\]\s\[flags:(.*?)\]/).join(',')
