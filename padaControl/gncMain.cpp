#include <iostream>
#include <Eigen/Dense>

// #include headers.hpp

int main(void) {

  // Startup
  runInits();
  getColor();
  
  // Pre-release loop
  while (hasReleased == false){
    pollSensors();
    updateState();
  }

  // Target Acquisition
  
  // Descent Loop

  // Flare & Land Loop

  // Shutdown

  return 0;
}