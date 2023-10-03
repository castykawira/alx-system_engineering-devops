#!/usr/bin/env ruby
# This Ruby script accepts one argument and checks if it exactly matches a string starting with 'h', ending with 'n', and having any single character in between
puts ARGV[0].scan(/h.n/).join
