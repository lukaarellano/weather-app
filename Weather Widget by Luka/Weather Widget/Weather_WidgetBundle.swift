//
//  Weather_WidgetBundle.swift
//  Weather Widget
//
//  Created by Luka Arellano on 12/27/25.
//

import WidgetKit
import SwiftUI

@main
struct Weather_WidgetBundle: WidgetBundle {
    var body: some Widget {
        Weather_Widget()
        Weather_WidgetControl()
    }
}
