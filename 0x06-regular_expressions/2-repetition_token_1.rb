#!/usr/bin/env ruby
# This Ruby script accepts one argument and matches the pattern "hb?tn" as per project requirements.
puts ARGV[0].scan(/hb?tn/).join
