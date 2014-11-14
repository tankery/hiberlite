{

    'targets': [
        {
            'target_name': 'hiberlite',
            'type': '<(component)',

            'include_dirs':[
                'include',
            ],

            'sources': [
                '<!@(ls src/*.cpp)',
            ],

            'dependencies': [
                'sqlite',
            ],

            'direct_dependent_settings': {
                'include_dirs':[
                    'include',
                ],

                'conditions': [
                    ['OS=="android"', {
                        'defines': [
                            'HL_NO_EXCEPTION_HANDLING',
                        ],
                    }],
                    ['OS=="ios"', {
                        'defines': [
                            'HL_NO_EXCEPTION_HANDLING',
                        ],
                    }],
                ],   # conditions
            },

            'conditions': [
                ['OS=="android"', {
                    'defines': [
                        'HL_NO_EXCEPTION_HANDLING',
                    ],
                }],
                ['OS=="ios"', {
                    'defines': [
                        'HL_NO_EXCEPTION_HANDLING',
                    ],
                    'xcode_settings': {
                        'SDKROOT': 'iphoneos',
                    },
                }],
            ],   # conditions

        },
        {
            'target_name': 'sqlite',
            'type': '<(component)',

            'include_dirs':[
                'sqlite-amalgamation',
            ],

            'sources': [
                'sqlite-amalgamation/sqlite3.c',
            ],

            'direct_dependent_settings': {
                'include_dirs':[
                    'sqlite-amalgamation',
                ],
            },

            'conditions': [
                ['OS=="ios"', {
                    'xcode_settings': {
                        'SDKROOT': 'iphoneos',
                    },
                }],
            ],   # conditions

        },
    ],

    'target_defaults': {
        # Things get confused if multiple targets in the same .gyp file don't have the same configuration
        # names, so define them all here.  (this problem doesn't appear to exist across .gyp files,
        # and it doesn't work to define configurations in globals.gypi).
        'default_configuration': 'Debug',
        'configurations': {
            'Debug': {
            },
            'Release': {
            },
        },

        'conditions': [
            ['OS=="android"', {
                'defines': [
                    'ANDROID',
                ],
            }],
            ['OS=="ios"', {
                'xcode_settings': {
                    'TARGETED_DEVICE_FAMILY': '1,2',
                    'CODE_SIGN_IDENTITY': 'iPhone Developer',
                    'IPHONEOS_DEPLOYMENT_TARGET': '7.1',
                },
            }], # OS=="ios"
        ],   # conditions
    },

}
