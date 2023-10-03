#!/usr/bin/env ruby
# This Ruby script accepts one argument and checks if it exactly matches a 10-digit phone number.
puts ARGV[0].scan(/^[0-9]{10}$/).join
