# For the list in the key, [other_name, extracellular or intracellular, significance in identifying this cell type, molecules expressed per cell]
# May need to assign value to extracellular and intracellular e.g. Ex=0.8, in=1, due to Intracellular antigens are usually dimmer and/or less discrete populations than surface antigens. 
# Criteria need to add (staining index,brightness index)
# t_natural_killer_cell=Natural killer T cell
# basophil 

astrocyte = {'CD40':['','ex',0,],
             'CD80':['','ex',0,],
             'CD86':['','ex',0,],
             'CD88':['','ex',0,],
             'GFAP':['','ex',0,],
             'S100B':['','in',0,],
            }

basophil = {'CD13':['','ex',0,],
            'CD44':['','ex',0,],
            'CD54':['','ex',0,],
            'CD63':['','ex',0,],
            'CD69':['','ex',0,],
            'CD107a':['','ex',0,],
            'CD123':['','ex',0,],
            'CD193':['CD193 (CCR3)','ex',0,],
            'CD203c':['','ex',0,],
            'FcεRIα':['','ex',0,],
            'IgE':['','ex',0,],
            'TLR4':['','ex',0,],}

b_cell = {'CD5':['','ex',60,], 
          'CD19':['','ex',100,], 
          'CD20':['','ex',60,], 
          'CD23':['','ex',60,], 
          'CD38':['','ex',60,], 
          'CD45':['','ex',90,], 
          'FMC7':['','ex',60,], 
          'lg, ϰ light chain':['','ex',80,], 
          'lg, λ light chain':['','ex',80,],
         }

b_cell_activated = {'CD19':['','ex',0,], 
                'CD25':['','ex',0,], 
                'CD30':['','ex',0,], 
                '':['','ex',0,], 
                '':['','ex',0,], 
                '':['','ex',0,], 
                '':['','ex',0,],
               }

#Lin-1,Lin-2,Lin-3 are using same color
dendritic_cell = {'CD11c':['','ex',100,], 
                  'CD16':['','ex',80,],
                  'CD56':['','ex',80,],
                  'CD80':['','ex',99,],
                  'CD83':['','ex',99,],
                  'CD86':['','ex',99,],
                  'CD123':['','ex',100,],
                  'CD209':['','ex',99,], 
                  'HLA-DR':['','ex',100,], 
                  'Lin-1':['','ex',100,],
                  'Lin-2':['','ex',100,],
                  'Lin-3':['','ex',100,],
                 }

eosinophil = {'CD44':['','ex',0,], 
                '':['','ex',0,], 
                '':['','ex',0,], 
                '':['','ex',0,], 
                '':['','ex',0,], 
                '':['','ex',0,], 
                '':['','ex',0,],
               }

erythroblast = {'CD71':['','ex',0,], 
                '':['','ex',0,], 
                '':['','ex',0,], 
                '':['','ex',0,], 
                '':['','ex',0,], 
                '':['','ex',0,], 
                '':['','ex',0,],
               }

erythrocyte = {'CD71':['','ex',0,], 
                '':['','ex',0,], 
                '':['','ex',0,], 
                '':['','ex',0,], 
                '':['','ex',0,], 
                '':['','ex',0,], 
                '':['','ex',0,],
               }

hematopoietic_stem_cell = {'':['','ex',100,], 
                '':['','ex',0,], 
                '':['','ex',0,], 
                '':['','ex',0,], 
                '':['','ex',0,], 
                '':['','ex',0,], 
                '':['','ex',0,],
               }

lymphoid_prgenitor_cell = {'':['','ex',80,], 
                '':['','ex',100,], 
                '':['','ex',70,], 
                '':['','ex',100,], 
                '':['','ex',100,], 
                '':['','ex',33,], 
                '':['','ex',100,], 
                '':['','ex',99,],
               }

macrophage = {'':['','ex',0,], 
              '':['','ex',0,], 
              '':['','ex',0,], 
              '':['','ex',0,], 
              '':['','ex',0,], 
              '':['','ex',0,], 
              '':['','ex',0,],
              }

mast_cell = {'CD117':['','ex',0,], 
             '':['','ex',0,], 
             '':['','ex',0,], 
             '':['','ex',0,], 
             '':['','ex',0,], 
             '':['','ex',0,], 
             '':['','ex',0,],
            }

megakaryocyte = {'CD61':['','ex',0,], 
                '':['','ex',0,], 
                '':['','ex',0,], 
                '':['','ex',0,], 
                '':['','ex',0,], 
                '':['','ex',0,], 
                '':['','ex',0,],
               }

monocyte = {'':['','ex',0,], 
            '':['','ex',0,], 
            '':['','ex',0,], 
            '':['','ex',0,], 
            '':['','ex',0,], 
            '':['','ex',0,], 
            '':['','ex',0,],
            }

myeloblast = {'CD138':['','ex',0,], 
              '':['','ex',0,], 
              '':['','ex',0,], 
              '':['','ex',0,], 
              '':['','ex',0,], 
              '':['','ex',0,], 
              '':['','ex',0,],
              }

myeloid_cell = {'CD11b':['','ex',80,], 
                'CD13':['','ex',100,], 
                'CD14':['','ex',70,], 
                'CD15':['','ex',100,], 
                'CD16':['','ex',100,], 
                'CD33':['','ex',33,], 
                'CD45':['','ex',100,], 
                'CD64':['','ex',99,],
               }

myeloid_dendritic_cell_total = {'CD1c':['','ex',0,], 
                                '':['CD141','ex',0,], 
                                '':['','ex',0,], 
                                '':['','ex',0,], 
                                '':['','ex',0,], 
                                '':['','ex',0,], 
                                '':['','ex',0,],
                                }

myeloid_dendritic_cell_1 = {'CD1c':['','ex',0,], 
                            '':['','ex',0,], 
                            '':['','ex',0,], 
                            '':['','ex',0,], 
                            '':['','ex',0,], 
                            '':['','ex',0,], 
                            '':['','ex',0,],
                            }

myeloid_dendritic_cell_2 = {'CD141':['','ex',0,], 
                            '':['','ex',0,], 
                            '':['','ex',0,], 
                            '':['','ex',0,], 
                            '':['','ex',0,], 
                            '':['','ex',0,], 
                            '':['','ex',0,],
                            }

myeloid_progenitor_cell = {'CD33':['','ex',0,], 
                           '':['','ex',0,], 
                           '':['','ex',0,], 
                           '':['','ex',0,], 
                           '':['','ex',0,], 
                           '':['','ex',0,], 
                           '':['','ex',0,],
                           }

natural_killer_cell = {'CD56':['','ex',100,], 
                '':['','ex',0,], 
                '':['','ex',0,], 
                '':['','ex',0,], 
                '':['','ex',0,], 
                '':['','ex',0,], 
                '':['','ex',0,],
               }

neutrophil = {'CD15':['','ex',0,],
              'CD16':['','ex',0,], 
              '':['','ex',0,], 
              '':['','ex',0,], 
              '':['','ex',0,], 
              '':['','ex',0,], 
              '':['','ex',0,],
              }

plasmacytoid_dendritic_cell = {'CD303':['','ex',100,], 
                'CD304':['','ex',0,], 
                '':['','ex',0,], 
                '':['','ex',0,], 
                '':['','ex',0,], 
                '':['','ex',0,], 
                '':['','ex',0,],
               }

plasma_cell = {'CD138':['','ex',0,], 
                '':['','ex',0,], 
                '':['','ex',0,], 
                '':['','ex',0,], 
                '':['','ex',0,], 
                '':['','ex',0,], 
                '':['','ex',0,],
               }

platelet = {'CD61':['','ex',0,], 
                '':['','ex',0,], 
                '':['','ex',0,], 
                '':['','ex',0,], 
                '':['','ex',0,], 
                '':['','ex',0,], 
                '':['','ex',0,],
               }

promonocyte = {'':['','ex',0,], 
               '':['','ex',0,], 
               '':['','ex',0,], 
               '':['','ex',0,], 
               '':['','ex',0,], 
               '':['','ex',0,], 
               '':['','ex',0,],
               }

# t_cytotoxic_cell = {'CD8':['','ex',100,], 
#                 '':['','ex',0,], 
#                 '':['','ex',0,], 
#                 '':['','ex',0,], 
#                 '':['','ex',0,], 
#                 '':['','ex',0,], 
#                 '':['','ex',0,],
#                }

# t_helper_cell = {'CD4':['','ex',100,], 
#                 '':['','ex',0,], 
#                 '':['','ex',0,], 
#                 '':['','ex',0,], 
#                 '':['','ex',0,], 
#                 '':['','ex',0,], 
#                 '':['','ex',0,],
#                }

# t_natural_killer_cell = {'CD3':['','ex',100,], 
#                 'CD56':['','ex',0,], 
#                 '':['','ex',0,], 
#                 '':['','ex',0,], 
#                 '':['','ex',0,], 
#                 '':['','ex',0,], 
#                 '':['','ex',0,],
#                }

# thymocyte = {'':['','ex',100,], 
#                 '':['','ex',0,], 
#                 '':['','ex',0,], 
#                 '':['','ex',0,], 
#                 '':['','ex',0,], 
#                 '':['','ex',0,], 
#                 '':['','ex',0,],
#                }

'''t_regulatory_cell = {'CD4':['','ex',0,],
         'CD25':['','ex',0,],
         'CD39':['','ex',0,],
         'CD62L':['','ex',0,],
         'CD73':['','ex',0,],
         'CD103':['','ex',0,],
         'CD134':['','ex',0,],
         'CD152 (CTLA-4)':['','ex',0,],
         'CD194 (CCR4)':['','ex',0,],
         'CD223':['','ex',0,],
         'FR4':['','ex',0,],
         'GARP':['','ex',0,],
         'GITR':['','ex',0,],
         'TGF-β':['','ex',0,],
         'FOXP3':['','ex',0,],
         'Helios':['','ex',0,],
        }
'''
total_t_cell = {'CD3':['','ex',90,1/124000], 
                'CD4':['','ex',80,1/100000], 
                'CD8':['','ex',80,1/90000], 
                'CD45':['','ex',100,1/200000], 
                'CD5':['','ex',70,1/90000], 
                'CD7':['','ex',0,1/20000], 
                'CD2':['','ex',0,1/55000],
               }

# For the list in the key, [other_name, extracellular or intracellular, significance in identifying this cell type, molecules expressed per cell]
