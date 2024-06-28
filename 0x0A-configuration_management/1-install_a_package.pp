#!/usr/bin/pup
# Install flask version 2.1.0

package { 'werkzeug':
  ensure   => '1.0.1',
  provider => 'pip3',
}

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Package['werkzeug'],
}
