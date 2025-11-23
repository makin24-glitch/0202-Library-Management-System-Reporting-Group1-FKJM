"""
Abstract base classes for the Library Management System.

This module defines the abstract interfaces that all concrete library classes must implement.
"""

from abc import ABC, abstractmethod

class AbstractLibraryItem(ABC):
  """ Abstract base class for all planting containers.
    
    This class defines the interface that all container types must implement,
    ensuring consistent behavior across different container types.
    """
  
  @abstractmethod
  def calculate_loan_period():
    """ Calculates the loan period 
        Returns: loan period
    """
    pass 

  @abstractmethod
  def calculate_replacement_cost():
    """ Calculates replacement costs
        Returns: replacement cost
    """
    pass
