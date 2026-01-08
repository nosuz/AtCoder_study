package abc438;

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.PrintStream;
import java.nio.charset.StandardCharsets;

class DTest {

    private static String stripLastNewline(String s) {
        // 末尾の改行だけを1個除去（\n / \r\n 対応）
        return s.replaceFirst("\\R\\z", "");
    }

    private static String show(String s) {
        // 見比べやすい表示（改行を可視化）
        return s.replace("\r", "\\\\r").replace("\n", "⏎\\n");
    }


    @Test
    void sample1() {
        String input = "5\r\n1 4 2 4 3\r\n2 3 4 2 2\r\n3 2 4 4 3";
        String expected = "16";

        // --- 標準入力を差し替え ---
        ByteArrayInputStream in =
            new ByteArrayInputStream(input.getBytes(StandardCharsets.UTF_8));
        System.setIn(in);

        // --- 標準出力をキャプチャ ---
        ByteArrayOutputStream out = new ByteArrayOutputStream();
        PrintStream originalOut = System.out;
        System.setOut(new PrintStream(out));

        try {
            D.main(new String[]{});
        } finally {
            System.setOut(originalOut);
        }

        // main() の出力は「末尾改行だけ」除去して expected と比較
        String resultRaw = out.toString(StandardCharsets.UTF_8);
        String result = stripLastNewline(resultRaw);

        assertEquals(
            expected,
            result,
            "\n--- DIFF ---\n"
            + "expected: [" + show(expected) + "]\n"
            + "result  : [" + show(result) + "]\n"
        );    }


    @Test
    void sample2() {
        String input = "3\r\n1 1 1\r\n1 1 1\r\n1 1 1";
        String expected = "3";

        // --- 標準入力を差し替え ---
        ByteArrayInputStream in =
            new ByteArrayInputStream(input.getBytes(StandardCharsets.UTF_8));
        System.setIn(in);

        // --- 標準出力をキャプチャ ---
        ByteArrayOutputStream out = new ByteArrayOutputStream();
        PrintStream originalOut = System.out;
        System.setOut(new PrintStream(out));

        try {
            D.main(new String[]{});
        } finally {
            System.setOut(originalOut);
        }

        // main() の出力は「末尾改行だけ」除去して expected と比較
        String resultRaw = out.toString(StandardCharsets.UTF_8);
        String result = stripLastNewline(resultRaw);

        assertEquals(
            expected,
            result,
            "\n--- DIFF ---\n"
            + "expected: [" + show(expected) + "]\n"
            + "result  : [" + show(result) + "]\n"
        );    }


    @Test
    void sample3() {
        String input = "6\r\n2 10 7 7 7 11\r\n5 7 9 10 9 12\r\n6 6 7 10 12 7";
        String expected = "50";

        // --- 標準入力を差し替え ---
        ByteArrayInputStream in =
            new ByteArrayInputStream(input.getBytes(StandardCharsets.UTF_8));
        System.setIn(in);

        // --- 標準出力をキャプチャ ---
        ByteArrayOutputStream out = new ByteArrayOutputStream();
        PrintStream originalOut = System.out;
        System.setOut(new PrintStream(out));

        try {
            D.main(new String[]{});
        } finally {
            System.setOut(originalOut);
        }

        // main() の出力は「末尾改行だけ」除去して expected と比較
        String resultRaw = out.toString(StandardCharsets.UTF_8);
        String result = stripLastNewline(resultRaw);

        assertEquals(
            expected,
            result,
            "\n--- DIFF ---\n"
            + "expected: [" + show(expected) + "]\n"
            + "result  : [" + show(result) + "]\n"
        );    }


}
