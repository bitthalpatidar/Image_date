// recognition parameters
        attribute SpeechGrammarList grammars;
        attribute DOMString lang;
        attribute boolean continuous;
        attribute boolean interimResults;
        attribute unsigned long maxAlternatives;
        attribute DOMString serviceURI;

        // methods to drive the speech interaction
        void start();
        void stop();
        void abort();

        // event methods
        attribute EventHandler onaudiostart;
        attribute EventHandler onsoundstart;
        attribute EventHandler onspeechstart;
        attribute EventHandler onspeechend;
        attribute EventHandler onsoundend;
        attribute EventHandler onaudioend;
        attribute EventHandler onresult;
        attribute EventHandler onnomatch;
        attribute EventHandler onerror;
        attribute EventHandler onstart;
        attribute EventHandler onend;
    };

    interface SpeechRecognitionError : Event {
        enum ErrorCode {
          "no-speech",
          "aborted",
          "audio-capture",
          "network",
          "not-allowed",
          "service-not-allowed",
          "bad-grammar",
          "language-not-supported"
        };

        readonly attribute ErrorCode error;
        readonly attribute DOMString message;
    };

    // Item in N-best list
    interface SpeechRecognitionAlternative {
        readonly attribute DOMString transcript;
        readonly attribute float confidence;
    };

    // A complete one-shot simple response
    interface SpeechRecognitionResult {
        readonly attribute unsigned long length;
        getter SpeechRecognitionAlternative item(in unsigned long index);
        readonly attribute boolean final;
    };

    // A collection of responses (used in continuous mode)
    interface SpeechRecognitionResultList {
        readonly attribute unsigned long length;
        getter SpeechRecognitionResult item(in unsigned long index);
    };

    // A full response, which could be interim or final, part of a continuous response or not
    interface SpeechRecognitionEvent : Event {
        readonly attribute unsigned long resultIndex;
        readonly attribute SpeechRecognitionResultList results;
        readonly attribute any interpretation;
        readonly attribute Document emma;
    };

    // The object representing a speech grammar
    [Constructor]
    interface SpeechGrammar {
        attribute DOMString src;
        attribute float weight;
    };

    // The object representing a speech grammar collection
    [Constructor]
    interface SpeechGrammarList {
        readonly attribute unsigned long length;
        getter SpeechGrammar item(in unsigned long index);
        void addFromURI(in DOMString src,
                        optional float weight);
        void addFromString(in DOMString string,
                        optional float weight);
    };

