'''
Defines a class, Neuron472440759, of neurons from Allen Brain Institute's model 472440759

A demo is available by running:

    python -i mosinit.py
'''
class Neuron472440759:
    def __init__(self, name="Neuron472440759", x=0, y=0, z=0):
        '''Instantiate Neuron472440759.
        
        Parameters:
            x, y, z -- position offset
            
        Note: if name is not specified, Neuron472440759_instance is used instead
        '''
            
        self._name = name
        # load the morphology
        from load_swc import load_swc
        load_swc('Sst-IRES-Cre_Ai14_IVSCC_-167636.04.01.01_475125280_m.swc', self,
                 use_axon=False, xshift=x, yshift=y, zshift=z)

        # custom axon (works because dropping axon during import)
        from neuron import h
        self.axon = [h.Section(cell=self, name='axon[0]'),
                     h.Section(cell=self, name='axon[1]')]
        for sec in self.axon:
            sec.L = 30
            sec.diam = 1
            sec.nseg = 1
        self.axon[0].connect(self.soma[0](0.5))
        self.axon[1].connect(self.axon[0](1))
        self.all += self.axon
    
        self._insert_mechanisms()
        self._discretize_model()
        self._set_mechanism_parameters()
    
    def __str__(self):
        if self._name is not None:
            return self._name
        else:
            return "Neuron472440759_instance"
                
    def _insert_mechanisms(self):
        from neuron import h
        for sec in self.all:
            sec.insert("pas")
        for mech in [u'CaDynamics', u'Ca_HVA', u'Ca_LVA', u'Ih', u'Im_v2', u'K_T', u'Kd', u'Kv2like', u'Kv3_1', u'NaV', u'SK']:
            self.soma[0].insert(mech)
    
    def _set_mechanism_parameters(self):
        from neuron import h
        for sec in self.all:
            sec.Ra = 137.63
            sec.e_pas = -88.4749730428
        
        for sec in self.axon:
            sec.cm = 1.57
            sec.g_pas = 0.000356143727022
        for sec in self.dend:
            sec.cm = 1.57
            sec.g_pas = 4.3458831865e-06
        for sec in self.soma:
            sec.cm = 1.57
            sec.ena = 53.0
            sec.ek = -107.0
            sec.gbar_Ih = 5.78157e-05
            sec.gbar_NaV = 0.098912
            sec.gbar_Kd = 0.000382101
            sec.gbar_Kv2like = 0.0439407
            sec.gbar_Kv3_1 = 0.273477
            sec.gbar_K_T = 0.00771644
            sec.gbar_Im_v2 = 4.84596e-05
            sec.gbar_SK = 0.000383302
            sec.gbar_Ca_HVA = 0.000842414
            sec.gbar_Ca_LVA = 0.00929033
            sec.gamma_CaDynamics = 0.00113282
            sec.decay_CaDynamics = 987.725
            sec.g_pas = 6.17182e-05
    
    def _discretize_model(self):
        for sec in self.all:
            sec.nseg = 1 + 2 * int(sec.L / 40)

