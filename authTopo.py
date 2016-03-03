from mininet.topo import Topo

class AuthTopo( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts
        host1 = self.addHost( 'h1' )
        host2 = self.addHost( 'h2' )
        host3 = self.addHost( 'h3' )

        # Add switches
        switch1 = self.addSwitch( 's4' )
        switch2 = self.addSwitch( 's5' )

        # Add links
        self.addLink( host1, switch1 )
        self.addLink( host2, switch1 )
        self.addLink( host3, switch1 )
        self.addLink( switch1, switch2 )

topos = { 'authtopo': ( lambda: AuthTopo() ) }