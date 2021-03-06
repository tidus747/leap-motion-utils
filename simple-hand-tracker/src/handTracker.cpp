/******************************************************************************\
 Simple Hand Tracker

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

Iván Rodríguez <piensa3d.dudas@gmail.com> 2020
\******************************************************************************/

#include <iostream>
#include <cstring>
#include "Leap.h"

using namespace Leap;

class SampleListener : public Listener {
  public:
    virtual void onInit(const Controller&);
    virtual void onConnect(const Controller&);
    virtual void onDisconnect(const Controller&);
    virtual void onExit(const Controller&);
    virtual void onFrame(const Controller&);
    virtual void onFocusGained(const Controller&);
    virtual void onFocusLost(const Controller&);
    virtual void onDeviceChange(const Controller&);
    virtual void onServiceConnect(const Controller&);
    virtual void onServiceDisconnect(const Controller&);

  private:
};

void SampleListener::onInit(const Controller& controller) {

}

void SampleListener::onConnect(const Controller& controller) {

}

void SampleListener::onDisconnect(const Controller& controller) {

}

void SampleListener::onExit(const Controller& controller) {
}

void SampleListener::onFrame(const Controller& controller) {
  // Get the most recent frame and report some basic information
  const Frame frame = controller.frame();
  std::cout << " " << frame.id()
            << " " << frame.timestamp()
            << " " << frame.hands().count()
            << " " << frame.fingers().extended().count() << std::flush;

  if (frame.hands().count() == 0){
    std::cout << "" << std::endl;
  }

  HandList hands = frame.hands();

  for (HandList::const_iterator hl = hands.begin(); hl != hands.end(); ++hl) {
    // Get the first hand
    const Hand hand = *hl;
    std::string handType = hand.isLeft() ? "L" : "R";
    if (frame.hands().count() == 1){
      std::cout << std::string(1, ' ') << handType << " " << hand.palmPosition() << std::endl;
    } else {
      std::cout << std::string(1, ' ') << handType << " " << hand.palmPosition() << std::flush;
    }

  }
  if (frame.hands().count() > 1){
    std::cout << "" << std::endl;
  }

}

void SampleListener::onFocusGained(const Controller& controller) {

}

void SampleListener::onFocusLost(const Controller& controller) {

}

void SampleListener::onDeviceChange(const Controller& controller) {
}

void SampleListener::onServiceConnect(const Controller& controller) {

}

void SampleListener::onServiceDisconnect(const Controller& controller) {

}

int main(int argc, char** argv) {
  // Create a sample listener and controller
  SampleListener listener;
  Controller controller;

  // Have the sample listener receive events from the controller
  controller.addListener(listener);

  if (argc > 1 && strcmp(argv[1], "--bg") == 0)
    controller.setPolicy(Leap::Controller::POLICY_BACKGROUND_FRAMES);

  std::cin.get();

  // Remove the sample listener when done
  controller.removeListener(listener);

  return 0;
}
