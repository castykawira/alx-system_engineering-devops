#!/usr/bin/env ruby
# This Ruby script accepts one argument and checks if it matches only capital letters.
puts ARGV[0].scan(/[A-Z]/).join
