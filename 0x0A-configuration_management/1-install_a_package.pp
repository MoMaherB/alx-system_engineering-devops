# Install flask version 2.1.0
#!/usr/bin/pup
package {'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
