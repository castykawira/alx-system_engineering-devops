#!/usr/bin/env ruby
# This Ruby script accepts one argument and matches the pattern "hbttn" as per project requirements
puts ARGV[0].scan(/hbt{2,5}n/).join
